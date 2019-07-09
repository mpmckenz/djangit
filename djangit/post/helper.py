from djangit.comment.models import Comment


def toggle_comment_upvotes(request):
    if 'upvote' in request.POST:
        comment = Comment.objects.get(id=request.POST['upvote'])
        if request.user.djangituser in comment.upvotes.all():
            comment.upvotes.remove(request.user.djangituser)
        else:
            comment.downvotes.remove(request.user.djangituser)
            comment.upvotes.add(request.user.djangituser)

    if 'downvote' in request.POST:
        comment = Comment.objects.get(id=request.POST['downvote'])
        if request.user.djangituser in comment.downvotes.all():
            comment.downvotes.remove(request.user.djangituser)
        else:
            comment.upvotes.remove(request.user.djangituser)
            comment.downvotes.add(request.user.djanituser)
        comment.save()
    return


# def sort_comments(comments):
#     sorted_comments = sorted(comments, reverse=True,
#                              key=lambda comment: comment.get_score())
#     return sorted_comments
