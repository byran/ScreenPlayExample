from behave import runner, step
from screenplay.matchers.contains import contains
from screenplay.condition import see_that
from tasks.search_for import search_for
from tasks.open_duckduckgo import open_duckduckgo
from questions.the_search_result_titles import the_search_result_titles
from screenplay_selenium.tasks import save_screenshot

# use_step_matcher("re")


@step(u'{actor} has opened DuckDuckGo')
def step_impl(context: runner.Context, actor: str):
    context.actors.switch_active(actor)
    context.they.attempt_to(
        open_duckduckgo()
    )


@step(u'they search for "{search_text}"')
def step_impl(context: runner.Context, search_text: str):
    context.they.attempt_to(
        search_for(search_text)
    )


@step(u"they should see a result for '{expected}'")
def step_impl(context: runner.Context, expected: str):
    context.they.should(
        see_that(the_search_result_titles(), contains(expected))
        .regardless_of_that(
            save_screenshot()
        )
    )
