from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization

from django.db.models import Q
from splitter.models import Profile, Profile_Friend, Group, Group_Friend, Expense, Expense_Splitter, Expense_Total, Settle
from django.db.models.query import QuerySet
import pickle
from itertools import chain
from tastypie.exceptions import Unauthorized


class Profile_Authorization(Authorization):
    # def read_list(self, object_list, bundle):
    #     #return object_list.filter(Q(profile_user__id=bundle.request.user)).distinct()
    #     return object_list.filter(Q(profile_user=bundle.request.user)).distinct()
    #
    # def read_detail(self, object_list, bundle):
    #     if object_list.filter(Q(profile_user=bundle.request.user)).distinct():
    #         return True
    #     else:
    #         return False
    #
    # def update_list(self, object_list, bundle):
    #     return object_list.filter(Q(profile_user=bundle.request.user)).distinct()
    #
    # def update_detail(self, object_list, bundle):
    #     if object_list.filter(Q(profile_user=bundle.request.user)).distinct():
    #         return True
    #     else:
    #         return False
    #
    # def delete_list(self, object_list, bundle):
    #     return object_list.filter(Q(profile_user=bundle.request.user)).distinct()
    #
    # def delete_detail(self, object_list, bundle):
    #     if object_list.filter(Q(profile_user=bundle.request.user)).distinct():
    #         return True
    #     else:
    #         return False
    #pass
    def read_list(self, object_list, bundle):
        #return object_list.filter(Q(profile_user__id=bundle.request.user)).distinct()
        return object_list.filter(Q(profile_user=bundle.request.user) | Q(profile_friends__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(profile_user=bundle.request.user) | Q(profile_friends__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(profile_user=bundle.request.user) | Q(profile_friends__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(profile_user=bundle.request.user) | Q(profile_friends__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(profile_user=bundle.request.user) | Q(profile_friends__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(profile_user=bundle.request.user) | Q(profile_friends__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False



class Profile_Friend_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        print(object_list)
        print(bundle)
        print(object_list.filter(Q(profile__profile_user=bundle.request.user)).distinct())
        print(object_list.filter(Q(user__id=bundle.request.user.id)).distinct())
        print(object_list.filter(Q(profile=bundle.request.user.id)).distinct())
        return object_list.filter(Q(profile__profile_user=bundle.request.user) | Q(user__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(profile__profile_user=bundle.request.user) | Q(user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(profile__profile_user=bundle.request.user) | Q(user__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(profile__profile_user=bundle.request.user) | Q(user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(profile__profile_user=bundle.request.user) | Q(user__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(profile__profile_user=bundle.request.user) | Q(user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False
    #pass

class Group_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(creator=bundle.request.user) | Q(group_friends__id=bundle.request.user.id) | Q(group_friends__user__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(creator=bundle.request.user) | Q(group_friends__id=bundle.request.user.id) | Q(group_friends__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(creator=bundle.request.user) | Q(group_friends__id=bundle.request.user.id) | Q(group_friends__user__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(creator=bundle.request.user) | Q(group_friends__id=bundle.request.user.id) | Q(group_friends__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(creator=bundle.request.user) | Q(group_friends__id=bundle.request.user.id) | Q(group_friends__user__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(creator=bundle.request.user) | Q(group_friends__id=bundle.request.user.id) | Q(group_friends__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False
    #pass

class Group_Friend_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        print(object_list.filter(Q(friend__user__id=bundle.request.user.id)).distinct())
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id) | Q(friend__user__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id) | Q(friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id) | Q(friend__user__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id) | Q(friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id) | Q(friend__user__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id) | Q(friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False
    #pass



class Expense_Authorization(Authorization):
    def get_profile_friend(self, bundle):
        #raise Unauthorized(f"Hii read{profile_friend_user}")
        return Profile_Friend.objects.filter(user=bundle.request.user)

    def read_list(self, object_list, bundle):
        # profile_friend_user = self.get_profile_friend(bundle)
        # # raise Unauthorized(f"Hii{profile_friend_user}")
        # print("Hii")
        # print(f"Hii{profile_friend_user}")
        #print (object_list)
        #print ("in read list")
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__friend__user__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        #print (len(object_list))
        #print("in read detail")
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return True

    def update_list(self, object_list, bundle):
        #print("in update list")
        #print(object_list)
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__friend__user__id=bundle.request.user.id)).distinct()
        # return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__e_splitter__friend__id=bundle.request.user.id) | Q(group__group_friends__user__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        #print("in update detail")
        # print(object_list.filter(Q(splitters)))
        #if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__friend__user__id=bundle.request.user.id)).distinct():
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__e_splitter__friend__user__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False
    #pass

class Expense_Splitter_Authorization(Authorization):


    def read_list(self, object_list, bundle):
        return object_list.filter(Q(expense__group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(e_splitter__id=bundle.request.user.id) | Q(e_splitter__friend__user__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(expense__group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(e_splitter__id=bundle.request.user.id) | Q(e_splitter__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        #return object_list.filter(Q(expense__group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(e_splitter__id=bundle.request.user.id) | Q(e_splitter__friend__user__id=bundle.request.user.id)).distinct()
        return object_list.filter(
            Q(expense__group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(
                e_splitter__id=bundle.request.user.id) | Q(
                e_splitter__friend__user__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(expense__group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(e_splitter__id=bundle.request.user.id) | Q(e_splitter__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(expense__group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(e_splitter__id=bundle.request.user.id) | Q(e_splitter__friend__user__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(expense__group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(e_splitter__id=bundle.request.user.id) | Q(e_splitter__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False
    #pass



class Expense_Total_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(sender__friend__user__id=bundle.request.user.id) | Q(receiver__friend__user__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(sender__friend__user__id=bundle.request.user.id) | Q(receiver__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(sender__friend__user__id=bundle.request.user.id) | Q(receiver__friend__user__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(sender__friend__user__id=bundle.request.user.id) | Q(receiver__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(sender__friend__user__id=bundle.request.user.id) | Q(receiver__friend__user__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(sender__friend__user__id=bundle.request.user.id) | Q(receiver__friend__user__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False
    #pass


class Settle_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(expense__splitters__id=bundle.request.user.id) |
                              Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(expense__splitters__id=bundle.request.user.id) |
                              Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(expense__splitters__id=bundle.request.user.id) |
                                  Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(expense__splitters__id=bundle.request.user.id) |
                                  Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(expense__splitters__id=bundle.request.user.id) |
                                  Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creator__id=bundle.request.user.id) | Q(expense__payer__id=bundle.request.user.id) | Q(expense__splitters__id=bundle.request.user.id) |
                                  Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct():
            return True
        else:
            return False
    #pass
