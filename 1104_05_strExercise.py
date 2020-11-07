
#s = input().split()

s='''the grown-ups' response, this time,
was to advise me to lay aside my drawings of boa constrictors,
whether from the inside or the outside,
and devote myself instead to geography, history, arithmetic, and grammar.
That is why, at the, age of six, I gave up what might have been a magnificent
career as a painter.
I had been disheartened by the failure of my Drawing Number One and my Drawing
Number Two. Grown-ups never understand anything by themselves,
and it is tiresome for children to be always and forever explaining things
to the.'''

count = 0
l = s.split()
for c in l:
    if c.startswith('the'):
        print(c, end = ' ')
        if len(c)==3:
            count+=1
        elif not('a'<=c[3]<='z' or 'A'<=c[3]<='Z'):
            count+=1
print(count)


count = s.count('the ') + s.count('the,') + s.count('the.')

print(count)

