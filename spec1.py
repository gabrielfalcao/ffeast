# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sure import Feature


feature = Feature("HttpRequest should make requests")


with feature.background("Given an instance") as context:
    context.client = HttpRequest()


with feature.teardown() as context:
    user = getattr(context, 'user')


with feature.spec("It should implement the GET method") as context:
    context.client.get('/').should.be.a(Response)


with feature.spec("It should be possible to create new users") as context:

    # Given that I have a user manager"
    um = UserManager()

    # When I call the create method with the right arguments"
    context.user = um.create("lincoln", "secret321!1!1")

    # Then I check that the user has the right attributes
    user.name.should.equal("lincoln")
