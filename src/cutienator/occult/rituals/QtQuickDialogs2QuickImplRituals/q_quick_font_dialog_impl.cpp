//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/QSharedPointer>

//  const QMetaObject *QQuickFontDialogImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickFontDialogImpl10metaObjectEv(
    const QQuickFontDialogImpl *self) {
  return self->metaObject();
}

//  void *QQuickFontDialogImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickFontDialogImpl11qt_metacastEPKc(
    QQuickFontDialogImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFontDialogImpl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickFontDialogImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFontDialogImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFontDialogImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickFontDialogImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFontDialogImpl::tr(s, c, n));
}

//  void QQuickFontDialogImpl::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl21qt_qmlMarker_attachedEv(
    QQuickFontDialogImpl *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickFontDialogImpl::QQuickFontDialogImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFontDialogImpl *ritual_ZN20QQuickFontDialogImplC1EP7QObject(
    QObject *parent) {
  return new QQuickFontDialogImpl(parent);
}

//  QQuickFontDialogImplAttached
//      *QQuickFontDialogImpl::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickFontDialogImplAttached *ritual_ZN20QQuickFontDialogImpl21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickFontDialogImpl::qmlAttachedProperties(object);
}

//  QSharedPointer<QFontDialogOptions> QQuickFontDialogImpl::options() const
extern "C" Q_DECL_EXPORT
QSharedPointer<QFontDialogOptions> *ritual_ZNK20QQuickFontDialogImpl7optionsEv(
    const QQuickFontDialogImpl *self) {
  return new QSharedPointer<QFontDialogOptions>(self->options());
}

//  void QQuickFontDialogImpl::setOptions(const
//      QSharedPointer<QFontDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl10setOptionsERK14QSharedPointerI18QFontDialogOptionsE(
    QQuickFontDialogImpl *self,
    const QSharedPointer<QFontDialogOptions> *options) {
  self->setOptions(*options);
}

//  QFont QQuickFontDialogImpl::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK20QQuickFontDialogImpl11currentFontEv(
    const QQuickFontDialogImpl *self) {
  return new QFont(self->currentFont());
}

//  void QQuickFontDialogImpl::setCurrentFont(const QFont &font, bool
//      selectInListViews)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl14setCurrentFontERK5QFontb(
    QQuickFontDialogImpl *self,
    const QFont *font,
    bool selectInListViews) {
  self->setCurrentFont(*font, selectInListViews);
}

//  void QQuickFontDialogImpl::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl4initEv(QQuickFontDialogImpl *self) {
  self->init();
}

//  void QQuickFontDialogImpl::optionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl14optionsChangedEv(
    QQuickFontDialogImpl *self) {
  self->optionsChanged();
}

//  void QQuickFontDialogImpl::currentFontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl18currentFontChangedERK5QFont(
    QQuickFontDialogImpl *self,
    const QFont *font) {
  self->currentFontChanged(*font);
}

//  void QQuickFontDialogImpl::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl15keyReleaseEventEP9QKeyEvent(
    QQuickFontDialogImpl *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickFontDialogImpl::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl13focusOutEventEP11QFocusEvent(
    QQuickFontDialogImpl *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QQuickFontDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFontDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFontDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickFontDialogImplPrivate *QQuickFontDialogImpl::d_func()
extern "C" Q_DECL_EXPORT
QQuickFontDialogImplPrivate *ritual_ZN20QQuickFontDialogImpl6d_funcEv(
    QQuickFontDialogImpl *self) {
  return self->d_func();
}

//  const QQuickFontDialogImplPrivate *QQuickFontDialogImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFontDialogImplPrivate *ritual_ZNK20QQuickFontDialogImpl6d_funcEv(
    const QQuickFontDialogImpl *self) {
  return self->d_func();
}

//  void QQuickFontDialogImpl::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickFontDialogImpl15keyReleaseEventEP9QKeyEvent(
    QQuickFontDialogImpl *self,
    QKeyEvent *event) {
  self->QQuickFontDialogImpl::keyReleaseEvent(event);
}

//  void QQuickFontDialogImpl::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickFontDialogImpl13focusOutEventEP11QFocusEvent(
    QQuickFontDialogImpl *self,
    QFocusEvent *event) {
  self->QQuickFontDialogImpl::focusOutEvent(event);
}

//  void QQuickFontDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickFontDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFontDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->QQuickFontDialogImpl::itemChange(change, *data);
}

//  a QSharedPointer<QFontDialogOptions> a ritual of QQuickFontDialogImpl
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickFontDialogImpl__QSharedPointer_QFontDialogOptions(
    QSharedPointer<QFontDialogOptions> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
