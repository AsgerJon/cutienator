//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcombobox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcombobox.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtGui/qicon.h>

//  const QMetaObject *QComboBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QComboBox10metaObjectEv(
    const QComboBox *self) {
  return self->metaObject();
}

//  QString QComboBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QComboBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QComboBox::tr(s, c, n));
}

//  QComboBox::QComboBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QComboBox *ritual_ZN9QComboBoxC1EP7QWidget(QWidget *parent) {
  return new QComboBox(parent);
}

//  QComboBox::~QComboBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBoxD1Ev(QComboBox *self) {
  delete self;
}

//  int QComboBox::maxVisibleItems() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox15maxVisibleItemsEv(const QComboBox *self) {
  return self->maxVisibleItems();
}

//  void QComboBox::setMaxVisibleItems(int maxItems)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox18setMaxVisibleItemsEi(
    QComboBox *self,
    int maxItems) {
  self->setMaxVisibleItems(maxItems);
}

//  int QComboBox::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox5countEv(const QComboBox *self) {
  return self->count();
}

//  void QComboBox::setMaxCount(int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setMaxCountEi(QComboBox *self, int max) {
  self->setMaxCount(max);
}

//  int QComboBox::maxCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox8maxCountEv(const QComboBox *self) {
  return self->maxCount();
}

//  bool QComboBox::duplicatesEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QComboBox17duplicatesEnabledEv(const QComboBox *self) {
  return self->duplicatesEnabled();
}

//  void QComboBox::setDuplicatesEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox20setDuplicatesEnabledEb(
    QComboBox *self,
    bool enable) {
  self->setDuplicatesEnabled(enable);
}

//  void QComboBox::setFrame(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox8setFrameEb(QComboBox *self, bool a0) {
  self->setFrame(a0);
}

//  bool QComboBox::hasFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QComboBox8hasFrameEv(const QComboBox *self) {
  return self->hasFrame();
}

//  int QComboBox::findText(const QString &text, Qt::MatchFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox8findTextERK7QString6QFlagsIN2Qt9MatchFlagEE(
    const QComboBox *self,
    const QString *text,
    int flags) {
  return self->findText(*text, QFlags<Qt::MatchFlag>::fromInt(flags));
}

//  int QComboBox::findData(const QVariant &data, int role, Qt::MatchFlags
//      flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox8findDataERK8QVarianti6QFlagsIN2Qt9MatchFlagEE(
    const QComboBox *self,
    const QVariant *data,
    int role,
    int flags) {
  return self->findData(*data, role, QFlags<Qt::MatchFlag>::fromInt(flags));
}

//  InsertPolicy QComboBox::insertPolicy() const
extern "C" Q_DECL_EXPORT
QComboBox::InsertPolicy ritual_ZNK9QComboBox12insertPolicyEv(
    const QComboBox *self) {
  return self->insertPolicy();
}

//  void QComboBox::setInsertPolicy(InsertPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15setInsertPolicyENS_12InsertPolicyE(
    QComboBox *self,
    QComboBox::InsertPolicy policy) {
  self->setInsertPolicy(policy);
}

//  SizeAdjustPolicy QComboBox::sizeAdjustPolicy() const
extern "C" Q_DECL_EXPORT
QComboBox::SizeAdjustPolicy ritual_ZNK9QComboBox16sizeAdjustPolicyEv(
    const QComboBox *self) {
  return self->sizeAdjustPolicy();
}

//  void QComboBox::setSizeAdjustPolicy(SizeAdjustPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox19setSizeAdjustPolicyENS_16SizeAdjustPolicyE(
    QComboBox *self,
    QComboBox::SizeAdjustPolicy policy) {
  self->setSizeAdjustPolicy(policy);
}

//  int QComboBox::minimumContentsLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox21minimumContentsLengthEv(const QComboBox *self) {
  return self->minimumContentsLength();
}

//  void QComboBox::setMinimumContentsLength(int characters)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox24setMinimumContentsLengthEi(
    QComboBox *self,
    int characters) {
  self->setMinimumContentsLength(characters);
}

//  QSize QComboBox::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QComboBox8iconSizeEv(const QComboBox *self) {
  return new QSize(self->iconSize());
}

//  void QComboBox::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setIconSizeERK5QSize(
    QComboBox *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  void QComboBox::setPlaceholderText(const QString &placeholderText)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox18setPlaceholderTextERK7QString(
    QComboBox *self,
    const QString *placeholderText) {
  self->setPlaceholderText(*placeholderText);
}

//  QString QComboBox::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QComboBox15placeholderTextEv(const QComboBox *self) {
  return new QString(self->placeholderText());
}

//  bool QComboBox::isEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QComboBox10isEditableEv(const QComboBox *self) {
  return self->isEditable();
}

//  void QComboBox::setEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setEditableEb(QComboBox *self, bool editable) {
  self->setEditable(editable);
}

//  void QComboBox::setLineEdit(QLineEdit *edit)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setLineEditEP9QLineEdit(
    QComboBox *self,
    QLineEdit *edit) {
  self->setLineEdit(edit);
}

//  QLineEdit *QComboBox::lineEdit() const
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZNK9QComboBox8lineEditEv(const QComboBox *self) {
  return self->lineEdit();
}

//  void QComboBox::setValidator(const QValidator *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox12setValidatorEPK10QValidator(
    QComboBox *self,
    const QValidator *v) {
  self->setValidator(v);
}

//  const QValidator *QComboBox::validator() const
extern "C" Q_DECL_EXPORT
const QValidator *ritual_ZNK9QComboBox9validatorEv(const QComboBox *self) {
  return self->validator();
}

//  void QComboBox::setCompleter(QCompleter *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox12setCompleterEP10QCompleter(
    QComboBox *self,
    QCompleter *c) {
  self->setCompleter(c);
}

//  QCompleter *QComboBox::completer() const
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZNK9QComboBox9completerEv(const QComboBox *self) {
  return self->completer();
}

//  QAbstractItemDelegate *QComboBox::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK9QComboBox12itemDelegateEv(
    const QComboBox *self) {
  return self->itemDelegate();
}

//  void QComboBox::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15setItemDelegateEP21QAbstractItemDelegate(
    QComboBox *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemModel *QComboBox::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK9QComboBox5modelEv(const QComboBox *self) {
  return self->model();
}

//  void QComboBox::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox8setModelEP18QAbstractItemModel(
    QComboBox *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QModelIndex QComboBox::rootModelIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK9QComboBox14rootModelIndexEv(const QComboBox *self) {
  return new QModelIndex(self->rootModelIndex());
}

//  void QComboBox::setRootModelIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox17setRootModelIndexERK11QModelIndex(
    QComboBox *self,
    const QModelIndex *index) {
  self->setRootModelIndex(*index);
}

//  int QComboBox::modelColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox11modelColumnEv(const QComboBox *self) {
  return self->modelColumn();
}

//  void QComboBox::setModelColumn(int visibleColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox14setModelColumnEi(
    QComboBox *self,
    int visibleColumn) {
  self->setModelColumn(visibleColumn);
}

//  LabelDrawingMode QComboBox::labelDrawingMode() const
extern "C" Q_DECL_EXPORT
QComboBox::LabelDrawingMode ritual_ZNK9QComboBox16labelDrawingModeEv(
    const QComboBox *self) {
  return self->labelDrawingMode();
}

//  void QComboBox::setLabelDrawingMode(LabelDrawingMode labelDrawing)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox19setLabelDrawingModeENS_16LabelDrawingModeE(
    QComboBox *self,
    QComboBox::LabelDrawingMode labelDrawing) {
  self->setLabelDrawingMode(labelDrawing);
}

//  int QComboBox::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QComboBox12currentIndexEv(const QComboBox *self) {
  return self->currentIndex();
}

//  QString QComboBox::currentText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QComboBox11currentTextEv(const QComboBox *self) {
  return new QString(self->currentText());
}

//  QVariant QComboBox::currentData(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox11currentDataEi(
    const QComboBox *self,
    int role) {
  return new QVariant(self->currentData(role));
}

//  QString QComboBox::itemText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QComboBox8itemTextEi(const QComboBox *self, int index) {
  return new QString(self->itemText(index));
}

//  QIcon QComboBox::itemIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK9QComboBox8itemIconEi(const QComboBox *self, int index) {
  return new QIcon(self->itemIcon(index));
}

//  QVariant QComboBox::itemData(int index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox8itemDataEii(
    const QComboBox *self,
    int index,
    int role) {
  return new QVariant(self->itemData(index, role));
}

//  void QComboBox::addItem(const QString &text, const QVariant &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox7addItemERK7QStringRK8QVariant(
    QComboBox *self,
    const QString *text,
    const QVariant *userData) {
  self->addItem(*text, *userData);
}

//  void QComboBox::addItem(const QIcon &icon, const QString &text, const
//      QVariant &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox7addItemERK5QIconRK7QStringRK8QVariant(
    QComboBox *self,
    const QIcon *icon,
    const QString *text,
    const QVariant *userData) {
  self->addItem(*icon, *text, *userData);
}

//  void QComboBox::insertItem(int index, const QString &text, const QVariant
//      &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10insertItemEiRK7QStringRK8QVariant(
    QComboBox *self,
    int index,
    const QString *text,
    const QVariant *userData) {
  self->insertItem(index, *text, *userData);
}

//  void QComboBox::insertItem(int index, const QIcon &icon, const QString
//      &text, const QVariant &userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10insertItemEiRK5QIconRK7QStringRK8QVariant(
    QComboBox *self,
    int index,
    const QIcon *icon,
    const QString *text,
    const QVariant *userData) {
  self->insertItem(index, *icon, *text, *userData);
}

//  void QComboBox::insertSeparator(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15insertSeparatorEi(QComboBox *self, int index) {
  self->insertSeparator(index);
}

//  void QComboBox::removeItem(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox10removeItemEi(QComboBox *self, int index) {
  self->removeItem(index);
}

//  void QComboBox::setItemText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setItemTextEiRK7QString(
    QComboBox *self,
    int index,
    const QString *text) {
  self->setItemText(index, *text);
}

//  void QComboBox::setItemIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setItemIconEiRK5QIcon(
    QComboBox *self,
    int index,
    const QIcon *icon) {
  self->setItemIcon(index, *icon);
}

//  void QComboBox::setItemData(int index, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setItemDataEiRK8QVarianti(
    QComboBox *self,
    int index,
    const QVariant *value,
    int role) {
  self->setItemData(index, *value, role);
}

//  QAbstractItemView *QComboBox::view() const
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZNK9QComboBox4viewEv(const QComboBox *self) {
  return self->view();
}

//  void QComboBox::setView(QAbstractItemView *itemView)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox7setViewEP17QAbstractItemView(
    QComboBox *self,
    QAbstractItemView *itemView) {
  self->setView(itemView);
}

//  QSize QComboBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QComboBox8sizeHintEv(const QComboBox *self) {
  return new QSize(self->sizeHint());
}

//  QSize QComboBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QComboBox15minimumSizeHintEv(const QComboBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QComboBox::showPopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox9showPopupEv(QComboBox *self) {
  self->showPopup();
}

//  void QComboBox::hidePopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox9hidePopupEv(QComboBox *self) {
  self->hidePopup();
}

//  bool QComboBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QComboBox5eventEP6QEvent(QComboBox *self, QEvent *event) {
  return self->event(event);
}

//  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QComboBox *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->inputMethodQuery(a0));
}

//  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery query, const
//      QVariant &argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QComboBox16inputMethodQueryEN2Qt16InputMethodQueryERK8QVariant(
    const QComboBox *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}

//  void QComboBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox5clearEv(QComboBox *self) {
  self->clear();
}

//  void QComboBox::clearEditText()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox13clearEditTextEv(QComboBox *self) {
  self->clearEditText();
}

//  void QComboBox::setEditText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox11setEditTextERK7QString(
    QComboBox *self,
    const QString *text) {
  self->setEditText(*text);
}

//  void QComboBox::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox15setCurrentIndexEi(QComboBox *self, int index) {
  self->setCurrentIndex(index);
}

//  void QComboBox::setCurrentText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QComboBox14setCurrentTextERK7QString(
    QComboBox *self,
    const QString *text) {
  self->setCurrentText(*text);
}
