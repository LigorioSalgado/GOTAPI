from rest_framework import permissions

class ApiUserPermissions(permissions.BasePermission):

	SELECTED_GRUPO = "Los Chidos"

	def has_permission(self,request,view):
		print(request.user.username)
		if request.user.groups.filter(
			name=self.SELECTED_GRUPO
			) and request.method == 'GET':
			return True

		return False 

