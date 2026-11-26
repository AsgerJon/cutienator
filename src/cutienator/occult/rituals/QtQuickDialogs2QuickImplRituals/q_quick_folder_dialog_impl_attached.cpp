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

//  const QMetaObject *QQuickFolderDialogImplAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuickFolderDialogImplAttached10metaObjectEv(
    const QQuickFolderDialogImplAttached *self) {
  return self->metaObject();
}

//  void *QQuickFolderDialogImplAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QQuickFolderDialogImplAttached11qt_metacastEPKc(
    QQuickFolderDialogImplAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFolderDialogImplAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QQuickFolderDialogImplAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFolderDialogImplAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFolderDialogImplAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuickFolderDialogImplAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFolderDialogImplAttached::tr(s, c, n));
}

//  QQuickFolderDialogImplAttached::QQuickFolderDialogImplAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplAttached *ritual_ZN30QQuickFolderDialogImplAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickFolderDialogImplAttached(parent);
}

//  QQuickListView *QQuickFolderDialogImplAttached::folderDialogListView()
//      const
extern "C" Q_DECL_EXPORT
QQuickListView *ritual_ZNK30QQuickFolderDialogImplAttached20folderDialogListViewEv(
    const QQuickFolderDialogImplAttached *self) {
  return self->folderDialogListView();
}

//  void
//      QQuickFolderDialogImplAttached::setFolderDialogListView(QQuickListVie
//      w *folderDialogListView)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickFolderDialogImplAttached23setFolderDialogListViewEP14QQuickListView(
    QQuickFolderDialogImplAttached *self,
    QQuickListView *folderDialogListView) {
  self->setFolderDialogListView(folderDialogListView);
}

//  QQuickFolderBreadcrumbBar
//      *QQuickFolderDialogImplAttached::breadcrumbBar() const
extern "C" Q_DECL_EXPORT
QQuickFolderBreadcrumbBar *ritual_ZNK30QQuickFolderDialogImplAttached13breadcrumbBarEv(
    const QQuickFolderDialogImplAttached *self) {
  return self->breadcrumbBar();
}

//  void QQuickFolderDialogImplAttached::setBreadcrumbBar(QQuickFolderBreadcr
//      umbBar *breadcrumbBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickFolderDialogImplAttached16setBreadcrumbBarEP25QQuickFolderBreadcrumbBar(
    QQuickFolderDialogImplAttached *self,
    QQuickFolderBreadcrumbBar *breadcrumbBar) {
  self->setBreadcrumbBar(breadcrumbBar);
}

//  void QQuickFolderDialogImplAttached::folderDialogListViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickFolderDialogImplAttached27folderDialogListViewChangedEv(
    QQuickFolderDialogImplAttached *self) {
  self->folderDialogListViewChanged();
}

//  void QQuickFolderDialogImplAttached::breadcrumbBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickFolderDialogImplAttached20breadcrumbBarChangedEv(
    QQuickFolderDialogImplAttached *self) {
  self->breadcrumbBarChanged();
}

//  QQuickFolderDialogImplAttachedPrivate
//      *QQuickFolderDialogImplAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplAttachedPrivate *ritual_ZN30QQuickFolderDialogImplAttached6d_funcEv(
    QQuickFolderDialogImplAttached *self) {
  return self->d_func();
}

//  const QQuickFolderDialogImplAttachedPrivate
//      *QQuickFolderDialogImplAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFolderDialogImplAttachedPrivate *ritual_ZNK30QQuickFolderDialogImplAttached6d_funcEv(
    const QQuickFolderDialogImplAttached *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
