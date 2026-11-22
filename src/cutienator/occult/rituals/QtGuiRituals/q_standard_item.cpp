//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qstandarditemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qvariant.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtGui/qfont.h>
#include <QtGui/qbrush.h>
#include <cstring>

//  A QStandardItem that Python can take functions over in. Every QStandardItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQStandardItemCall0)(const void *, int, int *);
typedef void (*CuteQStandardItemCall1)(const void *, const QModelRoleDataSpan *, int *);
typedef void (*CuteQStandardItemCall2)(const void *, const QVariant *, int, int *);
typedef void * (*CuteQStandardItemCall3)(const void *, int *);
typedef int (*CuteQStandardItemCall4)(const void *, int *);
class CuteQStandardItem : public QStandardItem {
public:
  using QStandardItem::QStandardItem;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QStandardItem4dataEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QStandardItem9multiDataE18QModelRoleDataSpan")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QStandardItem7setDataERK8QVarianti")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QStandardItem5cloneEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QStandardItem4typeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QVariant QStandardItem::data(int role) const
  QVariant data(int role) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStandardItemCall0 call = reinterpret_cast<CuteQStandardItemCall0>(taken[0]);
      const QVariant * given = call(this, role, &handled);
      if (handled && given) return *given;
    }
    return QStandardItem::data(role);
  }

  //  void QStandardItem::multiData(QModelRoleDataSpan roleDataSpan) const
  void multiData(QModelRoleDataSpan roleDataSpan) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStandardItemCall1 call = reinterpret_cast<CuteQStandardItemCall1>(taken[1]);
      call(this, &roleDataSpan, &handled);
      if (handled) return;
    }
    QStandardItem::multiData(roleDataSpan);
  }

  //  void QStandardItem::setData(const QVariant &value, int role)
  void setData(const QVariant &value, int role) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStandardItemCall2 call = reinterpret_cast<CuteQStandardItemCall2>(taken[2]);
      call(this, &value, role, &handled);
      if (handled) return;
    }
    QStandardItem::setData(value, role);
  }

  //  QStandardItem *QStandardItem::clone() const
  QStandardItem *clone() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQStandardItemCall3 call = reinterpret_cast<CuteQStandardItemCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QStandardItem *>(given);
    }
    return QStandardItem::clone();
  }

  //  int QStandardItem::type() const
  int type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStandardItemCall4 call = reinterpret_cast<CuteQStandardItemCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QStandardItem::type();
  }
};

//  QStandardItem::QStandardItem()
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN13QStandardItemC1Ev() {
  return new CuteQStandardItem();
}

//  QStandardItem::QStandardItem(const QString &text)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN13QStandardItemC1ERK7QString(const QString *text) {
  return new CuteQStandardItem(*text);
}

//  QStandardItem::QStandardItem(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN13QStandardItemC1ERK5QIconRK7QString(
    const QIcon *icon,
    const QString *text) {
  return new CuteQStandardItem(*icon, *text);
}

//  QStandardItem::QStandardItem(int rows, int columns)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN13QStandardItemC1Eii(int rows, int columns) {
  return new CuteQStandardItem(rows, columns);
}

//  QStandardItem::~QStandardItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItemD1Ev(QStandardItem *self) {
  delete self;
}

//  QVariant QStandardItem::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QStandardItem4dataEi(
    const QStandardItem *self,
    int role) {
  return new QVariant(self->data(role));
}

//  void QStandardItem::multiData(QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QStandardItem9multiDataE18QModelRoleDataSpan(
    const QStandardItem *self,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*roleDataSpan);
}

//  void QStandardItem::setData(const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem7setDataERK8QVarianti(
    QStandardItem *self,
    const QVariant *value,
    int role) {
  self->setData(*value, role);
}

//  void QStandardItem::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem9clearDataEv(QStandardItem *self) {
  self->clearData();
}

//  QString QStandardItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QStandardItem4textEv(const QStandardItem *self) {
  return new QString(self->text());
}

//  void QStandardItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem7setTextERK7QString(
    QStandardItem *self,
    const QString *text) {
  self->setText(*text);
}

//  QIcon QStandardItem::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK13QStandardItem4iconEv(const QStandardItem *self) {
  return new QIcon(self->icon());
}

//  void QStandardItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem7setIconERK5QIcon(
    QStandardItem *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  QString QStandardItem::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QStandardItem7toolTipEv(const QStandardItem *self) {
  return new QString(self->toolTip());
}

//  void QStandardItem::setToolTip(const QString &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem10setToolTipERK7QString(
    QStandardItem *self,
    const QString *toolTip) {
  self->setToolTip(*toolTip);
}

//  QString QStandardItem::statusTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QStandardItem9statusTipEv(const QStandardItem *self) {
  return new QString(self->statusTip());
}

//  void QStandardItem::setStatusTip(const QString &statusTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem12setStatusTipERK7QString(
    QStandardItem *self,
    const QString *statusTip) {
  self->setStatusTip(*statusTip);
}

//  QString QStandardItem::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QStandardItem9whatsThisEv(const QStandardItem *self) {
  return new QString(self->whatsThis());
}

//  void QStandardItem::setWhatsThis(const QString &whatsThis)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem12setWhatsThisERK7QString(
    QStandardItem *self,
    const QString *whatsThis) {
  self->setWhatsThis(*whatsThis);
}

//  QSize QStandardItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QStandardItem8sizeHintEv(const QStandardItem *self) {
  return new QSize(self->sizeHint());
}

//  void QStandardItem::setSizeHint(const QSize &sizeHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem11setSizeHintERK5QSize(
    QStandardItem *self,
    const QSize *sizeHint) {
  self->setSizeHint(*sizeHint);
}

//  QFont QStandardItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QStandardItem4fontEv(const QStandardItem *self) {
  return new QFont(self->font());
}

//  void QStandardItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem7setFontERK5QFont(
    QStandardItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  Qt::Alignment QStandardItem::textAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStandardItem13textAlignmentEv(const QStandardItem *self) {
  return static_cast<int>(self->textAlignment().toInt());
}

//  void QStandardItem::setTextAlignment(Qt::Alignment textAlignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem16setTextAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QStandardItem *self,
    int textAlignment) {
  self->setTextAlignment(QFlags<Qt::AlignmentFlag>::fromInt(textAlignment));
}

//  QBrush QStandardItem::background() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QStandardItem10backgroundEv(const QStandardItem *self) {
  return new QBrush(self->background());
}

//  void QStandardItem::setBackground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem13setBackgroundERK6QBrush(
    QStandardItem *self,
    const QBrush *brush) {
  self->setBackground(*brush);
}

//  QBrush QStandardItem::foreground() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QStandardItem10foregroundEv(const QStandardItem *self) {
  return new QBrush(self->foreground());
}

//  void QStandardItem::setForeground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem13setForegroundERK6QBrush(
    QStandardItem *self,
    const QBrush *brush) {
  self->setForeground(*brush);
}

//  Qt::CheckState QStandardItem::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK13QStandardItem10checkStateEv(
    const QStandardItem *self) {
  return self->checkState();
}

//  void QStandardItem::setCheckState(Qt::CheckState checkState)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem13setCheckStateEN2Qt10CheckStateE(
    QStandardItem *self,
    Qt::CheckState checkState) {
  self->setCheckState(checkState);
}

//  QString QStandardItem::accessibleText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QStandardItem14accessibleTextEv(
    const QStandardItem *self) {
  return new QString(self->accessibleText());
}

//  void QStandardItem::setAccessibleText(const QString &accessibleText)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem17setAccessibleTextERK7QString(
    QStandardItem *self,
    const QString *accessibleText) {
  self->setAccessibleText(*accessibleText);
}

//  QString QStandardItem::accessibleDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QStandardItem21accessibleDescriptionEv(
    const QStandardItem *self) {
  return new QString(self->accessibleDescription());
}

//  void QStandardItem::setAccessibleDescription(const QString
//      &accessibleDescription)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem24setAccessibleDescriptionERK7QString(
    QStandardItem *self,
    const QString *accessibleDescription) {
  self->setAccessibleDescription(*accessibleDescription);
}

//  Qt::ItemFlags QStandardItem::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStandardItem5flagsEv(const QStandardItem *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QStandardItem::setFlags(Qt::ItemFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE(
    QStandardItem *self,
    int flags) {
  self->setFlags(QFlags<Qt::ItemFlag>::fromInt(flags));
}

//  bool QStandardItem::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem9isEnabledEv(const QStandardItem *self) {
  return self->isEnabled();
}

//  void QStandardItem::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem10setEnabledEb(
    QStandardItem *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QStandardItem::isEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem10isEditableEv(const QStandardItem *self) {
  return self->isEditable();
}

//  void QStandardItem::setEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem11setEditableEb(
    QStandardItem *self,
    bool editable) {
  self->setEditable(editable);
}

//  bool QStandardItem::isSelectable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem12isSelectableEv(const QStandardItem *self) {
  return self->isSelectable();
}

//  void QStandardItem::setSelectable(bool selectable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem13setSelectableEb(
    QStandardItem *self,
    bool selectable) {
  self->setSelectable(selectable);
}

//  bool QStandardItem::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem11isCheckableEv(const QStandardItem *self) {
  return self->isCheckable();
}

//  void QStandardItem::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem12setCheckableEb(
    QStandardItem *self,
    bool checkable) {
  self->setCheckable(checkable);
}

//  bool QStandardItem::isAutoTristate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem14isAutoTristateEv(const QStandardItem *self) {
  return self->isAutoTristate();
}

//  void QStandardItem::setAutoTristate(bool tristate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem15setAutoTristateEb(
    QStandardItem *self,
    bool tristate) {
  self->setAutoTristate(tristate);
}

//  bool QStandardItem::isUserTristate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem14isUserTristateEv(const QStandardItem *self) {
  return self->isUserTristate();
}

//  void QStandardItem::setUserTristate(bool tristate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem15setUserTristateEb(
    QStandardItem *self,
    bool tristate) {
  self->setUserTristate(tristate);
}

//  bool QStandardItem::isDragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem13isDragEnabledEv(const QStandardItem *self) {
  return self->isDragEnabled();
}

//  void QStandardItem::setDragEnabled(bool dragEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem14setDragEnabledEb(
    QStandardItem *self,
    bool dragEnabled) {
  self->setDragEnabled(dragEnabled);
}

//  bool QStandardItem::isDropEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem13isDropEnabledEv(const QStandardItem *self) {
  return self->isDropEnabled();
}

//  void QStandardItem::setDropEnabled(bool dropEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem14setDropEnabledEb(
    QStandardItem *self,
    bool dropEnabled) {
  self->setDropEnabled(dropEnabled);
}

//  QStandardItem *QStandardItem::parent() const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK13QStandardItem6parentEv(
    const QStandardItem *self) {
  return self->parent();
}

//  int QStandardItem::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStandardItem3rowEv(const QStandardItem *self) {
  return self->row();
}

//  int QStandardItem::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStandardItem6columnEv(const QStandardItem *self) {
  return self->column();
}

//  QModelIndex QStandardItem::index() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK13QStandardItem5indexEv(const QStandardItem *self) {
  return new QModelIndex(self->index());
}

//  QStandardItemModel *QStandardItem::model() const
extern "C" Q_DECL_EXPORT
QStandardItemModel *ritual_ZNK13QStandardItem5modelEv(
    const QStandardItem *self) {
  return self->model();
}

//  int QStandardItem::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStandardItem8rowCountEv(const QStandardItem *self) {
  return self->rowCount();
}

//  void QStandardItem::setRowCount(int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem11setRowCountEi(QStandardItem *self, int rows) {
  self->setRowCount(rows);
}

//  int QStandardItem::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStandardItem11columnCountEv(const QStandardItem *self) {
  return self->columnCount();
}

//  void QStandardItem::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem14setColumnCountEi(
    QStandardItem *self,
    int columns) {
  self->setColumnCount(columns);
}

//  bool QStandardItem::hasChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStandardItem11hasChildrenEv(const QStandardItem *self) {
  return self->hasChildren();
}

//  QStandardItem *QStandardItem::child(int row, int column) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK13QStandardItem5childEii(
    const QStandardItem *self,
    int row,
    int column) {
  return self->child(row, column);
}

//  void QStandardItem::setChild(int row, int column, QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem8setChildEiiPS_(
    QStandardItem *self,
    int row,
    int column,
    QStandardItem *item) {
  self->setChild(row, column, item);
}

//  void QStandardItem::setChild(int row, QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem8setChildEiPS_(
    QStandardItem *self,
    int row,
    QStandardItem *item) {
  self->setChild(row, item);
}

//  void QStandardItem::insertRows(int row, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem10insertRowsEii(
    QStandardItem *self,
    int row,
    int count) {
  self->insertRows(row, count);
}

//  void QStandardItem::insertColumns(int column, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem13insertColumnsEii(
    QStandardItem *self,
    int column,
    int count) {
  self->insertColumns(column, count);
}

//  void QStandardItem::removeRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem9removeRowEi(QStandardItem *self, int row) {
  self->removeRow(row);
}

//  void QStandardItem::removeColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem12removeColumnEi(
    QStandardItem *self,
    int column) {
  self->removeColumn(column);
}

//  void QStandardItem::removeRows(int row, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem10removeRowsEii(
    QStandardItem *self,
    int row,
    int count) {
  self->removeRows(row, count);
}

//  void QStandardItem::removeColumns(int column, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem13removeColumnsEii(
    QStandardItem *self,
    int column,
    int count) {
  self->removeColumns(column, count);
}

//  void QStandardItem::insertRow(int row, QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem9insertRowEiPS_(
    QStandardItem *self,
    int row,
    QStandardItem *item) {
  self->insertRow(row, item);
}

//  void QStandardItem::appendRow(QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem9appendRowEPS_(
    QStandardItem *self,
    QStandardItem *item) {
  self->appendRow(item);
}

//  QStandardItem *QStandardItem::takeChild(int row, int column)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN13QStandardItem9takeChildEii(
    QStandardItem *self,
    int row,
    int column) {
  return self->takeChild(row, column);
}

//  void QStandardItem::sortChildren(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStandardItem12sortChildrenEiN2Qt9SortOrderE(
    QStandardItem *self,
    int column,
    Qt::SortOrder order) {
  self->sortChildren(column, order);
}

//  QStandardItem *QStandardItem::clone() const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK13QStandardItem5cloneEv(const QStandardItem *self) {
  return self->clone();
}

//  int QStandardItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStandardItem4typeEv(const QStandardItem *self) {
  return self->type();
}

//  a Python function taken by a CuteQStandardItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStandardItem(
    QStandardItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStandardItem *>(self)->take(key, call);
}

//  QVariant QStandardItem::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK13QStandardItem4dataEi(
    const QStandardItem *self,
    int role) {
  return new QVariant(self->QStandardItem::data(role));
}

//  void QStandardItem::multiData(QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QStandardItem9multiDataE18QModelRoleDataSpan(
    const QStandardItem *self,
    const QModelRoleDataSpan *roleDataSpan) {
  self->QStandardItem::multiData(*roleDataSpan);
}

//  void QStandardItem::setData(const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QStandardItem7setDataERK8QVarianti(
    QStandardItem *self,
    const QVariant *value,
    int role) {
  self->QStandardItem::setData(*value, role);
}

//  QStandardItem *QStandardItem::clone() const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_own_ZNK13QStandardItem5cloneEv(
    const QStandardItem *self) {
  return self->QStandardItem::clone();
}

//  int QStandardItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QStandardItem4typeEv(const QStandardItem *self) {
  return self->QStandardItem::type();
}
