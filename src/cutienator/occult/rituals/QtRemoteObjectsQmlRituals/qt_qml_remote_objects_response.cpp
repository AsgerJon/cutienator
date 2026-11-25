//  Written by hand on 2026-11-25 from
//  QtRemoteObjectsQml/6.12.0/QtRemoteObjectsQml/private/
//  qremoteobjectsqml_p.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again.
//  Qt builds the part only where QtNetwork has 'localserver' (and
//  QtQuick is there), so the file stands under QT_CONFIG(localserver).
//  A plain struct of two fields, 'promise' and 'timer', whose class
//  line has no export macro: only its implicit destructor is written,
//  which is inline.
//  Not written: its implicit constructors, which a class Qt does not
//  export does not get, and 'operator='.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(localserver)
#include <QtRemoteObjectsQml/6.12.0/QtRemoteObjectsQml/private/qremoteobjectsqml_p.h>

//  QtQmlRemoteObjectsResponse::~QtQmlRemoteObjectsResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QtQmlRemoteObjectsResponseD1Ev(
    QtQmlRemoteObjectsResponse *self) {
  delete self;
}

#endif  // QT_CONFIG(localserver)
