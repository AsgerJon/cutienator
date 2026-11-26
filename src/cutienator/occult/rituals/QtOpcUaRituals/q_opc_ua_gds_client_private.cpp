//  Written by hand on 2026-11-25 from
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuagdsclient_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  destructor is called, through the object. Not written: the
//  constructor and every other function (declared, not inline). The
//  whole file stands under the condition the part's CMakeLists.txt
//  builds the class under, with <QtOpcUa/qtopcua-config.h> included
//  before it as it defines the feature 'gds'.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuaglobal.h>
#include <QtOpcUa/qtopcua-config.h>
#if QT_CONFIG(gds) && QT_CONFIG(openssl) \
    && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
#include <QtOpcUa/QtOpcUa>
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuagdsclient_p.h>

//  QOpcUaGdsClientPrivate::~QOpcUaGdsClientPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaGdsClientPrivateD1Ev(
    QOpcUaGdsClientPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
