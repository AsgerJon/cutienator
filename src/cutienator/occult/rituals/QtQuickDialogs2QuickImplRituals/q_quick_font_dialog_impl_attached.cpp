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

//  const QMetaObject *QQuickFontDialogImplAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickFontDialogImplAttached10metaObjectEv(
    const QQuickFontDialogImplAttached *self) {
  return self->metaObject();
}

//  QString QQuickFontDialogImplAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuickFontDialogImplAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFontDialogImplAttached::tr(s, c, n));
}

//  QQuickFontDialogImplAttached::QQuickFontDialogImplAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickFontDialogImplAttached *ritual_ZN28QQuickFontDialogImplAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickFontDialogImplAttached(parent);
}

//  QQuickListView *QQuickFontDialogImplAttached::familyListView() const
extern "C" Q_DECL_EXPORT
QQuickListView *ritual_ZNK28QQuickFontDialogImplAttached14familyListViewEv(
    const QQuickFontDialogImplAttached *self) {
  return self->familyListView();
}

//  void QQuickFontDialogImplAttached::setFamilyListView(QQuickListView
//      *familyListView)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached17setFamilyListViewEP14QQuickListView(
    QQuickFontDialogImplAttached *self,
    QQuickListView *familyListView) {
  self->setFamilyListView(familyListView);
}

//  QQuickListView *QQuickFontDialogImplAttached::styleListView() const
extern "C" Q_DECL_EXPORT
QQuickListView *ritual_ZNK28QQuickFontDialogImplAttached13styleListViewEv(
    const QQuickFontDialogImplAttached *self) {
  return self->styleListView();
}

//  void QQuickFontDialogImplAttached::setStyleListView(QQuickListView
//      *styleListView)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached16setStyleListViewEP14QQuickListView(
    QQuickFontDialogImplAttached *self,
    QQuickListView *styleListView) {
  self->setStyleListView(styleListView);
}

//  QQuickListView *QQuickFontDialogImplAttached::sizeListView() const
extern "C" Q_DECL_EXPORT
QQuickListView *ritual_ZNK28QQuickFontDialogImplAttached12sizeListViewEv(
    const QQuickFontDialogImplAttached *self) {
  return self->sizeListView();
}

//  void QQuickFontDialogImplAttached::setSizeListView(QQuickListView
//      *sizeListView)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached15setSizeListViewEP14QQuickListView(
    QQuickFontDialogImplAttached *self,
    QQuickListView *sizeListView) {
  self->setSizeListView(sizeListView);
}

//  QQuickTextEdit *QQuickFontDialogImplAttached::sampleEdit() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit *ritual_ZNK28QQuickFontDialogImplAttached10sampleEditEv(
    const QQuickFontDialogImplAttached *self) {
  return self->sampleEdit();
}

//  void QQuickFontDialogImplAttached::setSampleEdit(QQuickTextEdit
//      *sampleEdit)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached13setSampleEditEP14QQuickTextEdit(
    QQuickFontDialogImplAttached *self,
    QQuickTextEdit *sampleEdit) {
  self->setSampleEdit(sampleEdit);
}

//  QQuickDialogButtonBox *QQuickFontDialogImplAttached::buttonBox() const
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBox *ritual_ZNK28QQuickFontDialogImplAttached9buttonBoxEv(
    const QQuickFontDialogImplAttached *self) {
  return self->buttonBox();
}

//  void QQuickFontDialogImplAttached::setButtonBox(QQuickDialogButtonBox
//      *buttonBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached12setButtonBoxEP21QQuickDialogButtonBox(
    QQuickFontDialogImplAttached *self,
    QQuickDialogButtonBox *buttonBox) {
  self->setButtonBox(buttonBox);
}

//  QQuickComboBox *QQuickFontDialogImplAttached::writingSystemComboBox()
//      const
extern "C" Q_DECL_EXPORT
QQuickComboBox *ritual_ZNK28QQuickFontDialogImplAttached21writingSystemComboBoxEv(
    const QQuickFontDialogImplAttached *self) {
  return self->writingSystemComboBox();
}

//  void
//      QQuickFontDialogImplAttached::setWritingSystemComboBox(QQuickComboBox
//      *writingSystemComboBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached24setWritingSystemComboBoxEP14QQuickComboBox(
    QQuickFontDialogImplAttached *self,
    QQuickComboBox *writingSystemComboBox) {
  self->setWritingSystemComboBox(writingSystemComboBox);
}

//  QQuickCheckBox *QQuickFontDialogImplAttached::underlineCheckBox() const
extern "C" Q_DECL_EXPORT
QQuickCheckBox *ritual_ZNK28QQuickFontDialogImplAttached17underlineCheckBoxEv(
    const QQuickFontDialogImplAttached *self) {
  return self->underlineCheckBox();
}

//  void QQuickFontDialogImplAttached::setUnderlineCheckBox(QQuickCheckBox
//      *underlineCheckBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached20setUnderlineCheckBoxEP14QQuickCheckBox(
    QQuickFontDialogImplAttached *self,
    QQuickCheckBox *underlineCheckBox) {
  self->setUnderlineCheckBox(underlineCheckBox);
}

//  QQuickCheckBox *QQuickFontDialogImplAttached::strikeoutCheckBox() const
extern "C" Q_DECL_EXPORT
QQuickCheckBox *ritual_ZNK28QQuickFontDialogImplAttached17strikeoutCheckBoxEv(
    const QQuickFontDialogImplAttached *self) {
  return self->strikeoutCheckBox();
}

//  void QQuickFontDialogImplAttached::setStrikeoutCheckBox(QQuickCheckBox
//      *strikethroughCheckBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached20setStrikeoutCheckBoxEP14QQuickCheckBox(
    QQuickFontDialogImplAttached *self,
    QQuickCheckBox *strikethroughCheckBox) {
  self->setStrikeoutCheckBox(strikethroughCheckBox);
}

//  QQuickTextField *QQuickFontDialogImplAttached::familyEdit() const
extern "C" Q_DECL_EXPORT
QQuickTextField *ritual_ZNK28QQuickFontDialogImplAttached10familyEditEv(
    const QQuickFontDialogImplAttached *self) {
  return self->familyEdit();
}

//  void QQuickFontDialogImplAttached::setFamilyEdit(QQuickTextField
//      *familyEdit)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached13setFamilyEditEP15QQuickTextField(
    QQuickFontDialogImplAttached *self,
    QQuickTextField *familyEdit) {
  self->setFamilyEdit(familyEdit);
}

//  QQuickTextField *QQuickFontDialogImplAttached::styleEdit() const
extern "C" Q_DECL_EXPORT
QQuickTextField *ritual_ZNK28QQuickFontDialogImplAttached9styleEditEv(
    const QQuickFontDialogImplAttached *self) {
  return self->styleEdit();
}

//  void QQuickFontDialogImplAttached::setStyleEdit(QQuickTextField
//      *styleEdit)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached12setStyleEditEP15QQuickTextField(
    QQuickFontDialogImplAttached *self,
    QQuickTextField *styleEdit) {
  self->setStyleEdit(styleEdit);
}

//  QQuickTextField *QQuickFontDialogImplAttached::sizeEdit() const
extern "C" Q_DECL_EXPORT
QQuickTextField *ritual_ZNK28QQuickFontDialogImplAttached8sizeEditEv(
    const QQuickFontDialogImplAttached *self) {
  return self->sizeEdit();
}

//  void QQuickFontDialogImplAttached::setSizeEdit(QQuickTextField *sizeEdit)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached11setSizeEditEP15QQuickTextField(
    QQuickFontDialogImplAttached *self,
    QQuickTextField *sizeEdit) {
  self->setSizeEdit(sizeEdit);
}

//  void QQuickFontDialogImplAttached::searchFamily(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached12searchFamilyERK7QString(
    QQuickFontDialogImplAttached *self,
    const QString *s) {
  self->searchFamily(*s);
}

//  void QQuickFontDialogImplAttached::searchStyle(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached11searchStyleERK7QString(
    QQuickFontDialogImplAttached *self,
    const QString *s) {
  self->searchStyle(*s);
}

//  void QQuickFontDialogImplAttached::clearSearch()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached11clearSearchEv(
    QQuickFontDialogImplAttached *self) {
  self->clearSearch();
}

//  void QQuickFontDialogImplAttached::updateFamilies()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached14updateFamiliesEv(
    QQuickFontDialogImplAttached *self) {
  self->updateFamilies();
}

//  void QQuickFontDialogImplAttached::selectFontInListViews(const QFont
//      &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached21selectFontInListViewsERK5QFont(
    QQuickFontDialogImplAttached *self,
    const QFont *font) {
  self->selectFontInListViews(*font);
}

//  void QQuickFontDialogImplAttached::updateStyles()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached12updateStylesEv(
    QQuickFontDialogImplAttached *self) {
  self->updateStyles();
}

//  void QQuickFontDialogImplAttached::updateSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached11updateSizesEv(
    QQuickFontDialogImplAttached *self) {
  self->updateSizes();
}

//  void QQuickFontDialogImplAttached::_q_familyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached16_q_familyChangedEv(
    QQuickFontDialogImplAttached *self) {
  self->_q_familyChanged();
}

//  void QQuickFontDialogImplAttached::_q_styleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached15_q_styleChangedEv(
    QQuickFontDialogImplAttached *self) {
  self->_q_styleChanged();
}

//  void QQuickFontDialogImplAttached::_q_sizeEdited()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached13_q_sizeEditedEv(
    QQuickFontDialogImplAttached *self) {
  self->_q_sizeEdited();
}

//  void QQuickFontDialogImplAttached::_q_sizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached14_q_sizeChangedEv(
    QQuickFontDialogImplAttached *self) {
  self->_q_sizeChanged();
}

//  void QQuickFontDialogImplAttached::_q_updateSample()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached15_q_updateSampleEv(
    QQuickFontDialogImplAttached *self) {
  self->_q_updateSample();
}

//  void QQuickFontDialogImplAttached::_q_writingSystemChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached23_q_writingSystemChangedEi(
    QQuickFontDialogImplAttached *self,
    int index) {
  self->_q_writingSystemChanged(index);
}

//  void QQuickFontDialogImplAttached::searchListView(const QString &s,
//      QQuickListView *listView)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFontDialogImplAttached14searchListViewERK7QStringP14QQuickListView(
    QQuickFontDialogImplAttached *self,
    const QString *s,
    QQuickListView *listView) {
  self->searchListView(*s, listView);
}

//  QQuickFontDialogImplAttachedPrivate
//      *QQuickFontDialogImplAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickFontDialogImplAttachedPrivate *ritual_ZN28QQuickFontDialogImplAttached6d_funcEv(
    QQuickFontDialogImplAttached *self) {
  return self->d_func();
}

//  const QQuickFontDialogImplAttachedPrivate
//      *QQuickFontDialogImplAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFontDialogImplAttachedPrivate *ritual_ZNK28QQuickFontDialogImplAttached6d_funcEv(
    const QQuickFontDialogImplAttached *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
