//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimp
//  l_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/QSharedPointer>

//  const QMetaObject *QQuickMessageDialogImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickMessageDialogImpl10metaObjectEv(
    const QQuickMessageDialogImpl *self) {
  return self->metaObject();
}

//  void *QQuickMessageDialogImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickMessageDialogImpl11qt_metacastEPKc(
    QQuickMessageDialogImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMessageDialogImpl::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickMessageDialogImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMessageDialogImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMessageDialogImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickMessageDialogImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMessageDialogImpl::tr(s, c, n));
}

//  void QQuickMessageDialogImpl::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMessageDialogImpl21qt_qmlMarker_attachedEv(
    QQuickMessageDialogImpl *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickMessageDialogImpl::QQuickMessageDialogImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImpl *ritual_ZN23QQuickMessageDialogImplC1EP7QObject(
    QObject *parent) {
  return new QQuickMessageDialogImpl(parent);
}

//  QQuickMessageDialogImplAttached
//      *QQuickMessageDialogImpl::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImplAttached *ritual_ZN23QQuickMessageDialogImpl21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickMessageDialogImpl::qmlAttachedProperties(object);
}

//  QSharedPointer<QMessageDialogOptions> QQuickMessageDialogImpl::options()
//      const
extern "C" Q_DECL_EXPORT
QSharedPointer<QMessageDialogOptions> *ritual_ZNK23QQuickMessageDialogImpl7optionsEv(
    const QQuickMessageDialogImpl *self) {
  return new QSharedPointer<QMessageDialogOptions>(self->options());
}

//  void QQuickMessageDialogImpl::setOptions(const
//      QSharedPointer<QMessageDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMessageDialogImpl10setOptionsERK14QSharedPointerI21QMessageDialogOptionsE(
    QQuickMessageDialogImpl *self,
    const QSharedPointer<QMessageDialogOptions> *options) {
  self->setOptions(*options);
}

//  bool QQuickMessageDialogImpl::showDetailedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickMessageDialogImpl16showDetailedTextEv(
    const QQuickMessageDialogImpl *self) {
  return self->showDetailedText();
}

//  QString QQuickMessageDialogImpl::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickMessageDialogImpl4textEv(
    const QQuickMessageDialogImpl *self) {
  return new QString(self->text());
}

//  QString QQuickMessageDialogImpl::informativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickMessageDialogImpl15informativeTextEv(
    const QQuickMessageDialogImpl *self) {
  return new QString(self->informativeText());
}

//  QString QQuickMessageDialogImpl::detailedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickMessageDialogImpl12detailedTextEv(
    const QQuickMessageDialogImpl *self) {
  return new QString(self->detailedText());
}

//  void QQuickMessageDialogImpl::buttonClicked(QPlatformDialogHelper::Standa
//      rdButton button, QPlatformDialogHelper::ButtonRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMessageDialogImpl13buttonClickedEN21QPlatformDialogHelper14StandardButtonENS0_10ButtonRoleE(
    QQuickMessageDialogImpl *self,
    QPlatformDialogHelper::StandardButton button,
    QPlatformDialogHelper::ButtonRole role) {
  self->buttonClicked(button, role);
}

//  void QQuickMessageDialogImpl::showDetailedTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMessageDialogImpl23showDetailedTextChangedEv(
    QQuickMessageDialogImpl *self) {
  self->showDetailedTextChanged();
}

//  void QQuickMessageDialogImpl::optionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMessageDialogImpl14optionsChangedEv(
    QQuickMessageDialogImpl *self) {
  self->optionsChanged();
}

//  void QQuickMessageDialogImpl::toggleShowDetailedText()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMessageDialogImpl22toggleShowDetailedTextEv(
    QQuickMessageDialogImpl *self) {
  self->toggleShowDetailedText();
}

//  void QQuickMessageDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMessageDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMessageDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickMessageDialogImplPrivate *QQuickMessageDialogImpl::d_func()
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImplPrivate *ritual_ZN23QQuickMessageDialogImpl6d_funcEv(
    QQuickMessageDialogImpl *self) {
  return self->d_func();
}

//  const QQuickMessageDialogImplPrivate *QQuickMessageDialogImpl::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickMessageDialogImplPrivate *ritual_ZNK23QQuickMessageDialogImpl6d_funcEv(
    const QQuickMessageDialogImpl *self) {
  return self->d_func();
}

//  void QQuickMessageDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickMessageDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMessageDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->QQuickMessageDialogImpl::itemChange(change, *data);
}

//  a QSharedPointer<QMessageDialogOptions> a ritual of
//      QQuickMessageDialogImpl gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickMessageDialogImpl__QSharedPointer_QMessageDialogOptions(
    QSharedPointer<QMessageDialogOptions> *self) {
  delete self;
}
