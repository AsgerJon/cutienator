//  Written by hand on 2026-11-25 from
//  QtRemoteObjectsQml/6.12.0/QtRemoteObjectsQml/private/
//  qremoteobjectsqml_p.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again.
//  Qt builds the part only where QtNetwork has 'localserver' (and
//  QtQuick is there), so the file stands under QT_CONFIG(localserver).
//  An empty struct whose class line has no export macro; it only
//  tells QML, by QML_FOREIGN, the name of QRemoteObjectNode.
//  Q_GADGET gives it staticMetaObject, a variable, and no function to
//  call: only its implicit destructor is written, which is inline.
//  Not written: its implicit constructors, which a class Qt does not
//  export does not get; 'operator='; qt_check_for_QGADGET_macro,
//  which Q_GADGET declares and nothing defines; qt_static_metacall,
//  moc's.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(localserver)
#include <QtRemoteObjectsQml/6.12.0/QtRemoteObjectsQml/private/qremoteobjectsqml_p.h>

//  QRemoteObjectNodeForeign::~QRemoteObjectNodeForeign()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectNodeForeignD1Ev(
    QRemoteObjectNodeForeign *self) {
  delete self;
}

#endif  // QT_CONFIG(localserver)
