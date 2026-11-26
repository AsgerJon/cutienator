//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if !defined(QT_NO_CONTEXTMENU)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QUnicodeControlCharacterMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QUnicodeControlCharacterMenu10metaObjectEv(
    const QUnicodeControlCharacterMenu *self) {
  return self->metaObject();
}

//  void *QUnicodeControlCharacterMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QUnicodeControlCharacterMenu11qt_metacastEPKc(
    QUnicodeControlCharacterMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QUnicodeControlCharacterMenu::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QUnicodeControlCharacterMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    QUnicodeControlCharacterMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QUnicodeControlCharacterMenu::menuActionTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QUnicodeControlCharacterMenu19menuActionTriggeredEv(
    QUnicodeControlCharacterMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QUnicodeControlCharacterMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuActionTriggered()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuActionTriggered()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // !defined(QT_NO_CONTEXTMENU)
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // QT_CONFIG(widgettextcontrol)
