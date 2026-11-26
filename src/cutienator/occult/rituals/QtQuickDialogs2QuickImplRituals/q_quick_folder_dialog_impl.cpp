//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/QSharedPointer>

//  const QMetaObject *QQuickFolderDialogImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickFolderDialogImpl10metaObjectEv(
    const QQuickFolderDialogImpl *self) {
  return self->metaObject();
}

//  void *QQuickFolderDialogImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickFolderDialogImpl11qt_metacastEPKc(
    QQuickFolderDialogImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFolderDialogImpl::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickFolderDialogImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFolderDialogImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFolderDialogImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickFolderDialogImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFolderDialogImpl::tr(s, c, n));
}

//  void QQuickFolderDialogImpl::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl21qt_qmlMarker_attachedEv(
    QQuickFolderDialogImpl *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickFolderDialogImpl::QQuickFolderDialogImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImpl *ritual_ZN22QQuickFolderDialogImplC1EP7QObject(
    QObject *parent) {
  return new QQuickFolderDialogImpl(parent);
}

//  QQuickFolderDialogImplAttached
//      *QQuickFolderDialogImpl::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplAttached *ritual_ZN22QQuickFolderDialogImpl21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickFolderDialogImpl::qmlAttachedProperties(object);
}

//  QUrl QQuickFolderDialogImpl::currentFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QQuickFolderDialogImpl13currentFolderEv(
    const QQuickFolderDialogImpl *self) {
  return new QUrl(self->currentFolder());
}

//  void QQuickFolderDialogImpl::setCurrentFolder(const QUrl &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl16setCurrentFolderERK4QUrl(
    QQuickFolderDialogImpl *self,
    const QUrl *folder) {
  self->setCurrentFolder(*folder);
}

//  QUrl QQuickFolderDialogImpl::selectedFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QQuickFolderDialogImpl14selectedFolderEv(
    const QQuickFolderDialogImpl *self) {
  return new QUrl(self->selectedFolder());
}

//  void QQuickFolderDialogImpl::setSelectedFolder(const QUrl
//      &selectedFolder)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl17setSelectedFolderERK4QUrl(
    QQuickFolderDialogImpl *self,
    const QUrl *selectedFolder) {
  self->setSelectedFolder(*selectedFolder);
}

//  QSharedPointer<QFileDialogOptions> QQuickFolderDialogImpl::options()
//      const
extern "C" Q_DECL_EXPORT
QSharedPointer<QFileDialogOptions> *ritual_ZNK22QQuickFolderDialogImpl7optionsEv(
    const QQuickFolderDialogImpl *self) {
  return new QSharedPointer<QFileDialogOptions>(self->options());
}

//  void QQuickFolderDialogImpl::setOptions(const
//      QSharedPointer<QFileDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl10setOptionsERK14QSharedPointerI18QFileDialogOptionsE(
    QQuickFolderDialogImpl *self,
    const QSharedPointer<QFileDialogOptions> *options) {
  self->setOptions(*options);
}

//  void QQuickFolderDialogImpl::setAcceptLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl14setAcceptLabelERK7QString(
    QQuickFolderDialogImpl *self,
    const QString *label) {
  self->setAcceptLabel(*label);
}

//  void QQuickFolderDialogImpl::setRejectLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl14setRejectLabelERK7QString(
    QQuickFolderDialogImpl *self,
    const QString *label) {
  self->setRejectLabel(*label);
}

//  void QQuickFolderDialogImpl::currentFolderChanged(const QUrl &folderUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl20currentFolderChangedERK4QUrl(
    QQuickFolderDialogImpl *self,
    const QUrl *folderUrl) {
  self->currentFolderChanged(*folderUrl);
}

//  void QQuickFolderDialogImpl::selectedFolderChanged(const QUrl &folderUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl21selectedFolderChangedERK4QUrl(
    QQuickFolderDialogImpl *self,
    const QUrl *folderUrl) {
  self->selectedFolderChanged(*folderUrl);
}

//  void QQuickFolderDialogImpl::nameFiltersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl18nameFiltersChangedEv(
    QQuickFolderDialogImpl *self) {
  self->nameFiltersChanged();
}

//  void QQuickFolderDialogImpl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl17componentCompleteEv(
    QQuickFolderDialogImpl *self) {
  self->componentComplete();
}

//  void QQuickFolderDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFolderDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFolderDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickFolderDialogImplPrivate *QQuickFolderDialogImpl::d_func()
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplPrivate *ritual_ZN22QQuickFolderDialogImpl6d_funcEv(
    QQuickFolderDialogImpl *self) {
  return self->d_func();
}

//  const QQuickFolderDialogImplPrivate *QQuickFolderDialogImpl::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickFolderDialogImplPrivate *ritual_ZNK22QQuickFolderDialogImpl6d_funcEv(
    const QQuickFolderDialogImpl *self) {
  return self->d_func();
}

//  void QQuickFolderDialogImpl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickFolderDialogImpl17componentCompleteEv(
    QQuickFolderDialogImpl *self) {
  self->QQuickFolderDialogImpl::componentComplete();
}

//  void QQuickFolderDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickFolderDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFolderDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->QQuickFolderDialogImpl::itemChange(change, *data);
}

//  a QSharedPointer<QFileDialogOptions> a ritual of QQuickFolderDialogImpl
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickFolderDialogImpl__QSharedPointer_QFileDialogOptions(
    QSharedPointer<QFileDialogOptions> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
