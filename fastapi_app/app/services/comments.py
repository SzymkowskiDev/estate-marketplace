from app.model.domain.comments import Comment
from app.model.domain.users import User


def check_user_can_modify_comment(comment: Comment, user: User) -> bool:
    return comment.author.username == user.username
