//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickFileDialogImplAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickFileDialogImplAttached10metaObjectEv(
    const QQuickFileDialogImplAttached *self) {
  return self->metaObject();
}

//  void *QQuickFileDialogImplAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickFileDialogImplAttached11qt_metacastEPKc(
    QQuickFileDialogImplAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFileDialogImplAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickFileDialogImplAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFileDialogImplAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFileDialogImplAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuickFileDialogImplAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFileDialogImplAttached::tr(s, c, n));
}

//  QQuickFileDialogImplAttached::QQuickFileDialogImplAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplAttached *ritual_ZN28QQuickFileDialogImplAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickFileDialogImplAttached(parent);
}

//  QQuickDialogButtonBox *QQuickFileDialogImplAttached::buttonBox() const
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBox *ritual_ZNK28QQuickFileDialogImplAttached9buttonBoxEv(
    const QQuickFileDialogImplAttached *self) {
  return self->buttonBox();
}

//  void QQuickFileDialogImplAttached::setButtonBox(QQuickDialogButtonBox
//      *buttonBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached12setButtonBoxEP21QQuickDialogButtonBox(
    QQuickFileDialogImplAttached *self,
    QQuickDialogButtonBox *buttonBox) {
  self->setButtonBox(buttonBox);
}

//  QQuickComboBox *QQuickFileDialogImplAttached::nameFiltersComboBox() const
extern "C" Q_DECL_EXPORT
QQuickComboBox *ritual_ZNK28QQuickFileDialogImplAttached19nameFiltersComboBoxEv(
    const QQuickFileDialogImplAttached *self) {
  return self->nameFiltersComboBox();
}

//  void QQuickFileDialogImplAttached::setNameFiltersComboBox(QQuickComboBox
//      *nameFiltersComboBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached22setNameFiltersComboBoxEP14QQuickComboBox(
    QQuickFileDialogImplAttached *self,
    QQuickComboBox *nameFiltersComboBox) {
  self->setNameFiltersComboBox(nameFiltersComboBox);
}

//  QQuickLabel *QQuickFileDialogImplAttached::filterLabel() const
extern "C" Q_DECL_EXPORT
QQuickLabel *ritual_ZNK28QQuickFileDialogImplAttached11filterLabelEv(
    const QQuickFileDialogImplAttached *self) {
  return self->filterLabel();
}

//  void QQuickFileDialogImplAttached::setFilterLabel(QQuickLabel *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached14setFilterLabelEP11QQuickLabel(
    QQuickFileDialogImplAttached *self,
    QQuickLabel *label) {
  self->setFilterLabel(label);
}

//  QString QQuickFileDialogImplAttached::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QQuickFileDialogImplAttached18selectedNameFilterEv(
    const QQuickFileDialogImplAttached *self) {
  return new QString(self->selectedNameFilter());
}

//  void QQuickFileDialogImplAttached::selectNameFilter(const QString
//      &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached16selectNameFilterERK7QString(
    QQuickFileDialogImplAttached *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  QQuickListView *QQuickFileDialogImplAttached::fileDialogListView() const
extern "C" Q_DECL_EXPORT
QQuickListView *ritual_ZNK28QQuickFileDialogImplAttached18fileDialogListViewEv(
    const QQuickFileDialogImplAttached *self) {
  return self->fileDialogListView();
}

//  void QQuickFileDialogImplAttached::setFileDialogListView(QQuickListView
//      *fileDialogListView)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached21setFileDialogListViewEP14QQuickListView(
    QQuickFileDialogImplAttached *self,
    QQuickListView *fileDialogListView) {
  self->setFileDialogListView(fileDialogListView);
}

//  QQuickFolderBreadcrumbBar *QQuickFileDialogImplAttached::breadcrumbBar()
//      const
extern "C" Q_DECL_EXPORT
QQuickFolderBreadcrumbBar *ritual_ZNK28QQuickFileDialogImplAttached13breadcrumbBarEv(
    const QQuickFileDialogImplAttached *self) {
  return self->breadcrumbBar();
}

//  void
//      QQuickFileDialogImplAttached::setBreadcrumbBar(QQuickFolderBreadcrumb
//      Bar *breadcrumbBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached16setBreadcrumbBarEP25QQuickFolderBreadcrumbBar(
    QQuickFileDialogImplAttached *self,
    QQuickFolderBreadcrumbBar *breadcrumbBar) {
  self->setBreadcrumbBar(breadcrumbBar);
}

//  QQuickLabel *QQuickFileDialogImplAttached::fileNameLabel() const
extern "C" Q_DECL_EXPORT
QQuickLabel *ritual_ZNK28QQuickFileDialogImplAttached13fileNameLabelEv(
    const QQuickFileDialogImplAttached *self) {
  return self->fileNameLabel();
}

//  void QQuickFileDialogImplAttached::setFileNameLabel(QQuickLabel
//      *fileNameLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached16setFileNameLabelEP11QQuickLabel(
    QQuickFileDialogImplAttached *self,
    QQuickLabel *fileNameLabel) {
  self->setFileNameLabel(fileNameLabel);
}

//  QQuickTextField *QQuickFileDialogImplAttached::fileNameTextField() const
extern "C" Q_DECL_EXPORT
QQuickTextField *ritual_ZNK28QQuickFileDialogImplAttached17fileNameTextFieldEv(
    const QQuickFileDialogImplAttached *self) {
  return self->fileNameTextField();
}

//  void QQuickFileDialogImplAttached::setFileNameTextField(QQuickTextField
//      *fileNameTextField)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached20setFileNameTextFieldEP15QQuickTextField(
    QQuickFileDialogImplAttached *self,
    QQuickTextField *fileNameTextField) {
  self->setFileNameTextField(fileNameTextField);
}

//  QQuickDialog *QQuickFileDialogImplAttached::overwriteConfirmationDialog()
//      const
extern "C" Q_DECL_EXPORT
QQuickDialog *ritual_ZNK28QQuickFileDialogImplAttached27overwriteConfirmationDialogEv(
    const QQuickFileDialogImplAttached *self) {
  return self->overwriteConfirmationDialog();
}

//  void
//      QQuickFileDialogImplAttached::setOverwriteConfirmationDialog(QQuickDi
//      alog *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached30setOverwriteConfirmationDialogEP12QQuickDialog(
    QQuickFileDialogImplAttached *self,
    QQuickDialog *dialog) {
  self->setOverwriteConfirmationDialog(dialog);
}

//  QQuickSideBar *QQuickFileDialogImplAttached::sideBar() const
extern "C" Q_DECL_EXPORT
QQuickSideBar *ritual_ZNK28QQuickFileDialogImplAttached7sideBarEv(
    const QQuickFileDialogImplAttached *self) {
  return self->sideBar();
}

//  void QQuickFileDialogImplAttached::setSideBar(QQuickSideBar *sideBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached10setSideBarEP13QQuickSideBar(
    QQuickFileDialogImplAttached *self,
    QQuickSideBar *sideBar) {
  self->setSideBar(sideBar);
}

//  void QQuickFileDialogImplAttached::buttonBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached16buttonBoxChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->buttonBoxChanged();
}

//  void QQuickFileDialogImplAttached::nameFiltersComboBoxChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached26nameFiltersComboBoxChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->nameFiltersComboBoxChanged();
}

//  void QQuickFileDialogImplAttached::filterLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached18filterLabelChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->filterLabelChanged();
}

//  void QQuickFileDialogImplAttached::fileDialogListViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached25fileDialogListViewChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->fileDialogListViewChanged();
}

//  void QQuickFileDialogImplAttached::breadcrumbBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached20breadcrumbBarChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->breadcrumbBarChanged();
}

//  void QQuickFileDialogImplAttached::fileNameLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached20fileNameLabelChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->fileNameLabelChanged();
}

//  void QQuickFileDialogImplAttached::fileNameTextFieldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached24fileNameTextFieldChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->fileNameTextFieldChanged();
}

//  void QQuickFileDialogImplAttached::overwriteConfirmationDialogChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached34overwriteConfirmationDialogChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->overwriteConfirmationDialogChanged();
}

//  void QQuickFileDialogImplAttached::sideBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFileDialogImplAttached14sideBarChangedEv(
    QQuickFileDialogImplAttached *self) {
  self->sideBarChanged();
}

//  QQuickFileDialogImplAttachedPrivate
//      *QQuickFileDialogImplAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplAttachedPrivate *ritual_ZN28QQuickFileDialogImplAttached6d_funcEv(
    QQuickFileDialogImplAttached *self) {
  return self->d_func();
}

//  const QQuickFileDialogImplAttachedPrivate
//      *QQuickFileDialogImplAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFileDialogImplAttachedPrivate *ritual_ZNK28QQuickFileDialogImplAttached6d_funcEv(
    const QQuickFileDialogImplAttached *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
