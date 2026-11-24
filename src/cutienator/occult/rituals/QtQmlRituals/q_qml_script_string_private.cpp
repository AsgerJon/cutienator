//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlscriptstring_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlscriptstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlscriptstring.h>
#include <QtCore/qstring.h>

//  QQmlScriptStringPrivate::QQmlScriptStringPrivate()
extern "C" Q_DECL_EXPORT
QQmlScriptStringPrivate *ritual_ZN23QQmlScriptStringPrivateC1Ev() {
  return new QQmlScriptStringPrivate();
}

//  const QQmlScriptStringPrivate *QQmlScriptStringPrivate::get(const
//      QQmlScriptString &script)
extern "C" Q_DECL_EXPORT
const QQmlScriptStringPrivate *ritual_ZN23QQmlScriptStringPrivate3getERK16QQmlScriptString(
    const QQmlScriptString *script) {
  return QQmlScriptStringPrivate::get(*script);
}

//  QQmlScriptString QQmlScriptStringPrivate::create(const QString &script,
//      QQmlContext *context, QObject *scope)
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZN23QQmlScriptStringPrivate6createERK7QStringP11QQmlContextP7QObject(
    const QString *script,
    QQmlContext *context,
    QObject *scope) {
  return new QQmlScriptString(
      QQmlScriptStringPrivate::create(
          *script,
          context,
          scope));
}

//  QQmlScriptStringPrivate::~QQmlScriptStringPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlScriptStringPrivateD1Ev(QQmlScriptStringPrivate *self) {
  delete self;
}
