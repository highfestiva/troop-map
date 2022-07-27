# Injust war troop movement reporting

Building v1 to allow Ukranian civilians to report on russian troop movements
in the Russo-Ukranian conflict. Should it prove useful to the Ukranian people,
it would be a simple thing to help other attacked peoples in future conflicts.

My thinking is that civilians might be able to help their army in close-
quarter combat by reporting where they've spotted enemy troops.

Only enemy whereabouts can be reported.

I have no idea about the usefulness of this idea. I guess trying is the best
way forward.


## Civilian feature ideas

### Add markers

Symbol markers for troops, vehicles, etc. (perhaps also drones, tanks, and so
forth, but I suspect most major conflicts these days have that intelligence
already) is the main purpose of the tool. It might also be nice if individuals
could report on how sure they are of the position reported, and how accurate
they believe their sighting is with regards to how many troops spotted, their
exact position and so on.

Perhaps also reporting any other events seen or heared of. Possibly adding
directional arrows if the movement direction can be understood. Perhaps also
allow for reporting of places where suspected war crimes have been committed.

Probably useful with a short note for each marker.

I think I'll also have a manually settable retention time on each marker, so
it will disappear automatically after some time, as intelligence about troop
movements in times of war won't stay relevant very long. It might be nice with
a feature of sifting through old reports, for understanding enemy strategy and
for research, but I find that feature to have less importance to begin with at
least.

### Translation

Native language would be useful in most countries, English I think would only
suffice in the West. I suppose using the browser language is (best) way?

### IP whitelisting or accounts

Restricting IPs from Russia and/or Belarus might be futile, but I don't
currently know what might be the best way. Possibly OpenID authentication,
for accounts which have a) been active for at least a few years, and b) are
non-Russian.

Banning of desinformation agents. Sort of like how Wikipedia does it I
suppose, but I still have too little knowledge of these things.

### Growing helpfulness

If reporting via cell phones works, and there is utility to the friendly army,
I think it should be enough to get the word out there to a few people and
hopefully viral spread will do the rest. Attacked civilians will always be
eager to help their own army.


## Defence feature ideas

### Latest overview

I don't know if reports are very useful, but seeing city-center coordinates
with some kind of accuracy might be useful for strikes or strike-teams? I
don't know anything about military things, so I'll be dabbling in the dark
until I get a handle of what is useful.

### Advancing/retreating

Historically, the enemy was very volnerable when retreating. I don't know if
that is still the case, but such things might be fairly easy to grasp. I
suppose understanding if they are dug down in trenches and so forth would also
be fairly easy to figure out?

### Large-scale movement

Understanding movement on group/platoon level might be very different from
scaling up. I don't know what an army desires most to know, but it would be
really nice if the map zoom level could somehow help out. As long as the
amount of data stored is relatively small, it should not be a problem.

### Evaluation

Perhaps I can get some feedback from some intelligence agency if I get things
rolling. Swedish FOI?


## Technical ideas

### DB

For DB I think I'll try to use some Google NOSQL DaaS or so to store
documents. Preferrably something free, but it's not a requirement. I suspect
it neither needs fast reads nor writes — since the amount of data should be
tiny.

### Testing grounds

I need somewhere I can develop new stuff without affecting the live map. I
don't exactly know how to do that off the top of my head, but perhaps keeping
two separate DB accounts: one for DEV and one for PROD?

### Spam prevention

I guess OpenID accounts, as I was thinking to help with fake info?

### Mobile support

Is key. I need to make sure it works on all relevant browsers+versions on the
smart phones out there. It should be fast, easy and slick to report in. The
accounts must be a minimal hassle for stressed people that are near the enemy.

### Domain name

I need to buy a domain name to ensure it's easy to find.

### Dynamic

Keeping the code small and movable to allow for transition to other databases
is important, as 


## Other

### Colab

How do I get other people involved? I've only done open-source projects on my
own in the past. I've never recruited either. We could use UX, Web, possibly
back-end (if I'm not able to do it myself), platform specialists (AWS or
whatever we decide to run on), security experts (for dropping desinformation
and spy accounts). And I guess anybody else who can help.

### Sponsoring

Major corporations might be able to pitch in to pay for servers, domain names
and what not. Perhaps for a proper DB and support for historical searches.
Server back-end. Maybe even some money for the people involved, although I
don't think anybody involved cares about the money. I don't know how to
distribute it we get many maintainers.

I don't know how to show what companies sponsor. Perhaps have an about page in
the desktop version?
