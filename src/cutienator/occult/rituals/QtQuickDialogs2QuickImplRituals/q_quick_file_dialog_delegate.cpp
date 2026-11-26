//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelega
//  te_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  Only a class built on QQuickFileDialogDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFileDialogDelegate : QQuickFileDialogDelegate {
  using QQuickFileDialogDelegate::keyReleaseEvent;
};

//  const QMetaObject *QQuickFileDialogDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickFileDialogDelegate10metaObjectEv(
    const QQuickFileDialogDelegate *self) {
  return self->metaObject();
}

//  void *QQuickFileDialogDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickFileDialogDelegate11qt_metacastEPKc(
    QQuickFileDialogDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFileDialogDelegate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickFileDialogDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFileDialogDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFileDialogDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickFileDialogDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFileDialogDelegate::tr(s, c, n));
}

//  QQuickFileDialogDelegate::QQuickFileDialogDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFileDialogDelegate *ritual_ZN24QQuickFileDialogDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickFileDialogDelegate(parent);
}

//  QQuickDialog *QQuickFileDialogDelegate::dialog() const
extern "C" Q_DECL_EXPORT
QQuickDialog *ritual_ZNK24QQuickFileDialogDelegate6dialogEv(
    const QQuickFileDialogDelegate *self) {
  return self->dialog();
}

//  void QQuickFileDialogDelegate::setDialog(QQuickDialog *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickFileDialogDelegate9setDialogEP12QQuickDialog(
    QQuickFileDialogDelegate *self,
    QQuickDialog *dialog) {
  self->setDialog(dialog);
}

//  QUrl QQuickFileDialogDelegate::file() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QQuickFileDialogDelegate4fileEv(
    const QQuickFileDialogDelegate *self) {
  return new QUrl(self->file());
}

//  void QQuickFileDialogDelegate::setFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickFileDialogDelegate7setFileERK4QUrl(
    QQuickFileDialogDelegate *self,
    const QUrl *file) {
  self->setFile(*file);
}

//  void QQuickFileDialogDelegate::dialogChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickFileDialogDelegate13dialogChangedEv(
    QQuickFileDialogDelegate *self) {
  self->dialogChanged();
}

//  void QQuickFileDialogDelegate::fileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickFileDialogDelegate11fileChangedEv(
    QQuickFileDialogDelegate *self) {
  self->fileChanged();
}

//  void QQuickFileDialogDelegate::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickFileDialogDelegate15keyReleaseEventEP9QKeyEvent(
    QQuickFileDialogDelegate *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  QQuickFileDialogDelegatePrivate *QQuickFileDialogDelegate::d_func()
extern "C" Q_DECL_EXPORT
QQuickFileDialogDelegatePrivate *ritual_ZN24QQuickFileDialogDelegate6d_funcEv(
    QQuickFileDialogDelegate *self) {
  return self->d_func();
}

//  const QQuickFileDialogDelegatePrivate *QQuickFileDialogDelegate::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickFileDialogDelegatePrivate *ritual_ZNK24QQuickFileDialogDelegate6d_funcEv(
    const QQuickFileDialogDelegate *self) {
  return self->d_func();
}

//  void QQuickFileDialogDelegate::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickFileDialogDelegate15keyReleaseEventEP9QKeyEvent(
    QQuickFileDialogDelegate *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickFileDialogDelegate *>(self)->OwnQQuickFileDialogDelegate::keyReleaseEvent(
      event);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
