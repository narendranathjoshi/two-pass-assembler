mov r1,r2
swi 0x11
mov r2, #123
dsfdf: mov r3, #256
add r1, r2, r4
bgt label
str r1, [r4]
label: add r1, r1, r1
a: mov r7, r4
sd: swi 0x01
abc: mov r5, #256