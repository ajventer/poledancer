DESTDIR=/usr
BINDIR=${DESTDIR}/bin
ui:
	pyuic5 -x poledancer_mainwindow.ui -o poledancer_mainwindow.py

run: ui
	chmod a+x poledancer.py
	./poledancer.py

install: ui
	mkdir -p ${DESTDIR}/share/poledancer
	cp -rf  *.py ${DESTDIR}/share/poledancer
	cp -rf poledancer ${BINDIR}
	chmod a+x ${BINDIR}/poledancer ${DESTDIR}/share/poleseeker/poledancer.py