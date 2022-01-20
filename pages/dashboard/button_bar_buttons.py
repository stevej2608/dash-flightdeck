
from pages.components import dropdownButton, dropdownLink
from pages.components.hero_icons import USER_ICON, WIDGET_ICON, UPLOAD_ICON, SECURITY_ICON, FIRE_ICON_DANGER


def newTasksButton():
    return dropdownButton([
        dropdownLink("Add User", USER_ICON),
        dropdownLink("Add Widget", WIDGET_ICON),
        dropdownLink("Upload Files", UPLOAD_ICON),
        dropdownLink("Preview Security", SECURITY_ICON),
        dropdownLink("Upgrade to Pro", FIRE_ICON_DANGER),
    ], "New Task", buttonColor="gray-800")
