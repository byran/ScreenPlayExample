from behave import runner, model
from screenplay.behave_extensions import add_screenplay_objects_to
from screenplay.log import Log
from screenplay_selenium.abilities.browse_the_web import browse_the_web
from screenplay_selenium.tasks import save_screenshot
from screenplay_selenium.actions._find_base_action import find_base_action
import os
import pathlib


def find_element_failure_actions():
    return [save_screenshot()]


def before_all(context: runner.Context):
    relativePath = context.config.userdata['save_screenshot.relative_path']
    save_screenshot.path = os.path.normpath(os.path.join(pathlib.Path(__file__).parent, relativePath))
    find_base_action.create_fail_actions_callback = find_element_failure_actions


def before_scenario(context: runner.Context, scenario: model.Scenario):
    Log.to_actions()
    add_screenplay_objects_to(context)
    context.actors.add_person_called('Byran').who_can(browse_the_web.using_Chrome())
    context.actors.switch_active('Byran')


def after_scenario(context: runner.Context, scenario: model.Scenario):
    context.actors.clean_up()
