//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumb
//  bar_p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumbbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumbbar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QQuickFolderBreadcrumbBar *QQuickFolderBreadcrumbBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFolderBreadcrumbBar *ritual_ZN32QQuickFolderBreadcrumbBarPrivate6q_funcEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  return self->q_func();
}

//  const QQuickFolderBreadcrumbBar
//      *QQuickFolderBreadcrumbBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickFolderBreadcrumbBar *ritual_ZNK32QQuickFolderBreadcrumbBarPrivate6q_funcEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->q_func();
}

//  QQuickItem
//      *QQuickFolderBreadcrumbBarPrivate::createDelegateItem(QQmlComponent
//      *component, const QVariantMap &initialProperties)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN32QQuickFolderBreadcrumbBarPrivate18createDelegateItemEP13QQmlComponentRK4QMapI7QString8QVariantE(
    QQuickFolderBreadcrumbBarPrivate *self,
    QQmlComponent *component,
    const QMap<QString, QVariant> *initialProperties) {
  return self->createDelegateItem(component, *initialProperties);
}

//  QString QQuickFolderBreadcrumbBarPrivate::folderBaseName(const QString
//      &folderPath)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuickFolderBreadcrumbBarPrivate14folderBaseNameERK7QString(
    const QString *folderPath) {
  return new QString(
      QQuickFolderBreadcrumbBarPrivate::folderBaseName(
          *folderPath));
}

//  QStringList QQuickFolderBreadcrumbBarPrivate::crumbPathsForFolder(const
//      QUrl &folder)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN32QQuickFolderBreadcrumbBarPrivate19crumbPathsForFolderERK4QUrl(
    const QUrl *folder) {
  return new QList<QString>(
      QQuickFolderBreadcrumbBarPrivate::crumbPathsForFolder(
          *folder));
}

//  void QQuickFolderBreadcrumbBarPrivate::repopulate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate10repopulateEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->repopulate();
}

//  void QQuickFolderBreadcrumbBarPrivate::crumbClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate12crumbClickedEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->crumbClicked();
}

//  void QQuickFolderBreadcrumbBarPrivate::folderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate13folderChangedEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->folderChanged();
}

//  void QQuickFolderBreadcrumbBarPrivate::cancelUpButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate14cancelUpButtonEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->cancelUpButton();
}

//  void QQuickFolderBreadcrumbBarPrivate::executeUpButton(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate15executeUpButtonEb(
    QQuickFolderBreadcrumbBarPrivate *self,
    bool complete) {
  self->executeUpButton(complete);
}

//  void QQuickFolderBreadcrumbBarPrivate::goUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate4goUpEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->goUp();
}

//  void QQuickFolderBreadcrumbBarPrivate::cancelTextField()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate15cancelTextFieldEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->cancelTextField();
}

//  void QQuickFolderBreadcrumbBarPrivate::executeTextField(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate16executeTextFieldEb(
    QQuickFolderBreadcrumbBarPrivate *self,
    bool complete) {
  self->executeTextField(complete);
}

//  void QQuickFolderBreadcrumbBarPrivate::toggleTextFieldVisibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate25toggleTextFieldVisibilityEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->toggleTextFieldVisibility();
}

//  void QQuickFolderBreadcrumbBarPrivate::textFieldAccepted()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate17textFieldAcceptedEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->textFieldAccepted();
}

//  void QQuickFolderBreadcrumbBarPrivate::textFieldVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate23textFieldVisibleChangedEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->textFieldVisibleChanged();
}

//  void QQuickFolderBreadcrumbBarPrivate::textFieldActiveFocusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate27textFieldActiveFocusChangedEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->textFieldActiveFocusChanged();
}

//  void QQuickFolderBreadcrumbBarPrivate::handleTextFieldShown()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate20handleTextFieldShownEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->handleTextFieldShown();
}

//  void QQuickFolderBreadcrumbBarPrivate::handleTextFieldHidden()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate21handleTextFieldHiddenEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->handleTextFieldHidden();
}

//  void QQuickFolderBreadcrumbBarPrivate::ungrabEditPathShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate22ungrabEditPathShortcutEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->ungrabEditPathShortcut();
}

//  QQuickFileDialogImpl *QQuickFolderBreadcrumbBarPrivate::asFileDialog()
//      const
extern "C" Q_DECL_EXPORT
QQuickFileDialogImpl *ritual_ZNK32QQuickFolderBreadcrumbBarPrivate12asFileDialogEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->asFileDialog();
}

//  QQuickFolderDialogImpl
//      *QQuickFolderBreadcrumbBarPrivate::asFolderDialog() const
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImpl *ritual_ZNK32QQuickFolderBreadcrumbBarPrivate14asFolderDialogEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->asFolderDialog();
}

//  bool QQuickFolderBreadcrumbBarPrivate::isFileDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickFolderBreadcrumbBarPrivate12isFileDialogEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->isFileDialog();
}

//  QUrl QQuickFolderBreadcrumbBarPrivate::dialogFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK32QQuickFolderBreadcrumbBarPrivate12dialogFolderEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return new QUrl(self->dialogFolder());
}

//  void QQuickFolderBreadcrumbBarPrivate::setDialogFolder(const QUrl
//      &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate15setDialogFolderERK4QUrl(
    QQuickFolderBreadcrumbBarPrivate *self,
    const QUrl *folder) {
  self->setDialogFolder(*folder);
}

//  qreal QQuickFolderBreadcrumbBarPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK32QQuickFolderBreadcrumbBarPrivate15getContentWidthEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->getContentWidth();
}

//  qreal QQuickFolderBreadcrumbBarPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK32QQuickFolderBreadcrumbBarPrivate16getContentHeightEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->getContentHeight();
}

//  void QQuickFolderBreadcrumbBarPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate13resizeContentEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->resizeContent();
}

//  void QQuickFolderBreadcrumbBarPrivate::itemGeometryChanged(QQuickItem
//      *item, QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickFolderBreadcrumbBarPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void
//      QQuickFolderBreadcrumbBarPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickFolderBreadcrumbBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void
//      QQuickFolderBreadcrumbBarPrivate::itemImplicitHeightChanged(QQuickIte
//      m *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickFolderBreadcrumbBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickFolderBreadcrumbBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  qreal QQuickFolderBreadcrumbBarPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK32QQuickFolderBreadcrumbBarPrivate15getContentWidthEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->QQuickFolderBreadcrumbBarPrivate::getContentWidth();
}

//  qreal QQuickFolderBreadcrumbBarPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK32QQuickFolderBreadcrumbBarPrivate16getContentHeightEv(
    const QQuickFolderBreadcrumbBarPrivate *self) {
  return self->QQuickFolderBreadcrumbBarPrivate::getContentHeight();
}

//  void QQuickFolderBreadcrumbBarPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate13resizeContentEv(
    QQuickFolderBreadcrumbBarPrivate *self) {
  self->QQuickFolderBreadcrumbBarPrivate::resizeContent();
}

//  void QQuickFolderBreadcrumbBarPrivate::itemGeometryChanged(QQuickItem
//      *item, QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickFolderBreadcrumbBarPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickFolderBreadcrumbBarPrivate::itemGeometryChanged(
      item,
      *change,
      *diff);
}

//  void
//      QQuickFolderBreadcrumbBarPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickFolderBreadcrumbBarPrivate *self,
    QQuickItem *item) {
  self->QQuickFolderBreadcrumbBarPrivate::itemImplicitWidthChanged(item);
}

//  void
//      QQuickFolderBreadcrumbBarPrivate::itemImplicitHeightChanged(QQuickIte
//      m *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickFolderBreadcrumbBarPrivate *self,
    QQuickItem *item) {
  self->QQuickFolderBreadcrumbBarPrivate::itemImplicitHeightChanged(item);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
