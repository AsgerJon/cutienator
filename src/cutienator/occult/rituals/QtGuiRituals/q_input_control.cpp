//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinputcontrol_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qinputcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QInputControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QInputControl10metaObjectEv(
    const QInputControl *self) {
  return self->metaObject();
}

//  void *QInputControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QInputControl11qt_metacastEPKc(
    QInputControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QInputControl::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QInputControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QInputControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QInputControl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QInputControl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputControl::tr(s, c, n));
}

//  QInputControl::QInputControl(Type type, QObject *parent)
extern "C" Q_DECL_EXPORT
QInputControl *ritual_ZN13QInputControlC1ENS_4TypeEP7QObject(
    QInputControl::Type type,
    QObject *parent) {
  return new QInputControl(type, parent);
}

//  bool QInputControl::isAcceptableInput(const QKeyEvent *event) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QInputControl17isAcceptableInputEPK9QKeyEvent(
    const QInputControl *self,
    const QKeyEvent *event) {
  return self->isAcceptableInput(event);
}

//  bool QInputControl::isCommonTextEditShortcut(const QKeyEvent *ke)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QInputControl24isCommonTextEditShortcutEPK9QKeyEvent(
    const QKeyEvent *ke) {
  return QInputControl::isCommonTextEditShortcut(ke);
}

//  QVariant QInputControl::selectionWrapper(QMimeData *mimeData)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN13QInputControl16selectionWrapperEP9QMimeData(
    QMimeData *mimeData) {
  return new QVariant(QInputControl::selectionWrapper(mimeData));
}

//  QMimeData *QInputControl::mimeDataForInputEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZN13QInputControl21mimeDataForInputEventEP17QInputMethodEvent(
    QInputMethodEvent *event) {
  return QInputControl::mimeDataForInputEvent(event);
}

//  QInputControl::QInputControl(Type type, QObjectPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QInputControl *ritual_ZN13QInputControlC1ENS_4TypeER14QObjectPrivateP7QObject(
    QInputControl::Type type,
    QObjectPrivate *dd,
    QObject *parent) {
  return new QInputControl(type, *dd, parent);
}
