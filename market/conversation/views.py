from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from . import models
from .forms import NewConversationMessageForm, UpdateConversationMessageForm
from django.contrib.auth.models import User


@login_required
def conversations(request):
    user = get_object_or_404(User, pk=request.user.id)
    conversations = user.conversations.all()
    return render(
        request, "conversation/conversations.html", {"conversations": conversations}
    )


@login_required
def conversation(request, id):
    # conversation = get_object_or_404(models.Conversation, pk=id)
    conversation = models.Conversation.objects.filter(
        participants__in=[request.user.id]
    ).get(pk=id)
    receivers = conversation.participants.exclude(id=request.user.id)

    if request.method == "POST":
        form = UpdateConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("conversation:conversation", id=conversation.id)
    else:
        form = UpdateConversationMessageForm()

    return render(
        request,
        "conversation/conversation.html",
        {
            "conversation": conversation,
            "receivers": receivers,
            "form": form,
        },
    )


@login_required
def create(request, item_id):
    item = get_object_or_404(models.Item, pk=item_id)

    if item.created_by == request.user:
        return redirect("dashboard:index")

    existing_conversation = models.Conversation.objects.filter(
        participants__in=[request.user.id], item=item
    ).first()

    if existing_conversation:
        return redirect("conversation:conversation", existing_conversation.id)

    if request.method == "POST":
        form = NewConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = models.Conversation.objects.create(item=item)
            conversation.participants.add(request.user)
            conversation.participants.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("conversation:conversation", id=conversation.id)
    else:
        form = NewConversationMessageForm()
        return render(
            request,
            "conversation/form.html",
            {"form": form, "title": "Send a message to start a new conversation!"},
        )
