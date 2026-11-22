//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtreewidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qfont.h>
#include <QtGui/qbrush.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QTreeWidgetItem that Python can take functions over in. Every QTreeWidgetItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQTreeWidgetItemCall0)(const void *, int *);
typedef const QVariant * (*CuteQTreeWidgetItemCall1)(const void *, int, int, int *);
typedef void (*CuteQTreeWidgetItemCall2)(const void *, int, int, const QVariant *, int *);
class CuteQTreeWidgetItem : public QTreeWidgetItem {
public:
  using QTreeWidgetItem::QTreeWidgetItem;
  CuteQTreeWidgetItem(const QTreeWidgetItem &other) : QTreeWidgetItem(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QTreeWidgetItem5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QTreeWidgetItem4dataEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QTreeWidgetItem7setDataEiiRK8QVariant")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QTreeWidgetItem *QTreeWidgetItem::clone() const
  QTreeWidgetItem *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTreeWidgetItemCall0 call = reinterpret_cast<CuteQTreeWidgetItemCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTreeWidgetItem *>(given);
    }
    return QTreeWidgetItem::clone();
  }

  //  QVariant QTreeWidgetItem::data(int column, int role) const
  QVariant data(int column, int role) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTreeWidgetItemCall1 call = reinterpret_cast<CuteQTreeWidgetItemCall1>(taken[1]);
      const QVariant * given = call(this, column, role, &handled);
      if (handled && given) return *given;
    }
    return QTreeWidgetItem::data(column, role);
  }

  //  void QTreeWidgetItem::setData(int column, int role, const QVariant
  //      &value)
  void setData(int column, int role, const QVariant &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTreeWidgetItemCall2 call = reinterpret_cast<CuteQTreeWidgetItemCall2>(taken[2]);
      call(this, column, role, &value, &handled);
      if (handled) return;
    }
    QTreeWidgetItem::setData(column, role, value);
  }
};

//  QTreeWidgetItem::QTreeWidgetItem(int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1Ei(int type) {
  return new CuteQTreeWidgetItem(type);
}

//  QTreeWidgetItem::QTreeWidgetItem(const QStringList &strings, int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1ERK5QListI7QStringEi(
    const QList<QString> *strings,
    int type) {
  return new CuteQTreeWidgetItem(*strings, type);
}

//  QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1EP11QTreeWidgeti(
    QTreeWidget *treeview,
    int type) {
  return new CuteQTreeWidgetItem(treeview, type);
}

//  QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, const QStringList
//      &strings, int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1EP11QTreeWidgetRK5QListI7QStringEi(
    QTreeWidget *treeview,
    const QList<QString> *strings,
    int type) {
  return new CuteQTreeWidgetItem(treeview, *strings, type);
}

//  QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, QTreeWidgetItem
//      *after, int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1EP11QTreeWidgetPS_i(
    QTreeWidget *treeview,
    QTreeWidgetItem *after,
    int type) {
  return new CuteQTreeWidgetItem(treeview, after, type);
}

//  QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent, int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1EPS_i(
    QTreeWidgetItem *parent,
    int type) {
  return new CuteQTreeWidgetItem(parent, type);
}

//  QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent, const
//      QStringList &strings, int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1EPS_RK5QListI7QStringEi(
    QTreeWidgetItem *parent,
    const QList<QString> *strings,
    int type) {
  return new CuteQTreeWidgetItem(parent, *strings, type);
}

//  QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent, QTreeWidgetItem
//      *after, int type)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1EPS_S0_i(
    QTreeWidgetItem *parent,
    QTreeWidgetItem *after,
    int type) {
  return new CuteQTreeWidgetItem(parent, after, type);
}

//  QTreeWidgetItem::QTreeWidgetItem(const QTreeWidgetItem &other)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItemC1ERKS_(
    const QTreeWidgetItem *other) {
  return new CuteQTreeWidgetItem(*other);
}

//  QTreeWidgetItem::~QTreeWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItemD1Ev(QTreeWidgetItem *self) {
  delete self;
}

//  QTreeWidgetItem *QTreeWidgetItem::clone() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK15QTreeWidgetItem5cloneEv(
    const QTreeWidgetItem *self) {
  return self->clone();
}

//  QTreeWidget *QTreeWidgetItem::treeWidget() const
extern "C" Q_DECL_EXPORT
QTreeWidget *ritual_ZNK15QTreeWidgetItem10treeWidgetEv(
    const QTreeWidgetItem *self) {
  return self->treeWidget();
}

//  void QTreeWidgetItem::setSelected(bool select)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem11setSelectedEb(
    QTreeWidgetItem *self,
    bool select) {
  self->setSelected(select);
}

//  bool QTreeWidgetItem::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTreeWidgetItem10isSelectedEv(const QTreeWidgetItem *self) {
  return self->isSelected();
}

//  void QTreeWidgetItem::setHidden(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem9setHiddenEb(
    QTreeWidgetItem *self,
    bool hide) {
  self->setHidden(hide);
}

//  bool QTreeWidgetItem::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTreeWidgetItem8isHiddenEv(const QTreeWidgetItem *self) {
  return self->isHidden();
}

//  void QTreeWidgetItem::setExpanded(bool expand)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem11setExpandedEb(
    QTreeWidgetItem *self,
    bool expand) {
  self->setExpanded(expand);
}

//  bool QTreeWidgetItem::isExpanded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTreeWidgetItem10isExpandedEv(const QTreeWidgetItem *self) {
  return self->isExpanded();
}

//  void QTreeWidgetItem::setFirstColumnSpanned(bool span)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem21setFirstColumnSpannedEb(
    QTreeWidgetItem *self,
    bool span) {
  self->setFirstColumnSpanned(span);
}

//  bool QTreeWidgetItem::isFirstColumnSpanned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTreeWidgetItem20isFirstColumnSpannedEv(
    const QTreeWidgetItem *self) {
  return self->isFirstColumnSpanned();
}

//  void QTreeWidgetItem::setDisabled(bool disabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem11setDisabledEb(
    QTreeWidgetItem *self,
    bool disabled) {
  self->setDisabled(disabled);
}

//  bool QTreeWidgetItem::isDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTreeWidgetItem10isDisabledEv(const QTreeWidgetItem *self) {
  return self->isDisabled();
}

//  void QTreeWidgetItem::setChildIndicatorPolicy(QTreeWidgetItem::ChildIndic
//      atorPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem23setChildIndicatorPolicyENS_20ChildIndicatorPolicyE(
    QTreeWidgetItem *self,
    QTreeWidgetItem::ChildIndicatorPolicy policy) {
  self->setChildIndicatorPolicy(policy);
}

//  QTreeWidgetItem::ChildIndicatorPolicy
//      QTreeWidgetItem::childIndicatorPolicy() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem::ChildIndicatorPolicy ritual_ZNK15QTreeWidgetItem20childIndicatorPolicyEv(
    const QTreeWidgetItem *self) {
  return self->childIndicatorPolicy();
}

//  Qt::ItemFlags QTreeWidgetItem::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTreeWidgetItem5flagsEv(const QTreeWidgetItem *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QTreeWidgetItem::setFlags(Qt::ItemFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE(
    QTreeWidgetItem *self,
    int flags) {
  self->setFlags(QFlags<Qt::ItemFlag>::fromInt(flags));
}

//  QString QTreeWidgetItem::text(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTreeWidgetItem4textEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QString(self->text(column));
}

//  void QTreeWidgetItem::setText(int column, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem7setTextEiRK7QString(
    QTreeWidgetItem *self,
    int column,
    const QString *text) {
  self->setText(column, *text);
}

//  QIcon QTreeWidgetItem::icon(int column) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK15QTreeWidgetItem4iconEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QIcon(self->icon(column));
}

//  void QTreeWidgetItem::setIcon(int column, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem7setIconEiRK5QIcon(
    QTreeWidgetItem *self,
    int column,
    const QIcon *icon) {
  self->setIcon(column, *icon);
}

//  QString QTreeWidgetItem::statusTip(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTreeWidgetItem9statusTipEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QString(self->statusTip(column));
}

//  void QTreeWidgetItem::setStatusTip(int column, const QString &statusTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem12setStatusTipEiRK7QString(
    QTreeWidgetItem *self,
    int column,
    const QString *statusTip) {
  self->setStatusTip(column, *statusTip);
}

//  QString QTreeWidgetItem::toolTip(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTreeWidgetItem7toolTipEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QString(self->toolTip(column));
}

//  void QTreeWidgetItem::setToolTip(int column, const QString &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem10setToolTipEiRK7QString(
    QTreeWidgetItem *self,
    int column,
    const QString *toolTip) {
  self->setToolTip(column, *toolTip);
}

//  QString QTreeWidgetItem::whatsThis(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTreeWidgetItem9whatsThisEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QString(self->whatsThis(column));
}

//  void QTreeWidgetItem::setWhatsThis(int column, const QString &whatsThis)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem12setWhatsThisEiRK7QString(
    QTreeWidgetItem *self,
    int column,
    const QString *whatsThis) {
  self->setWhatsThis(column, *whatsThis);
}

//  QFont QTreeWidgetItem::font(int column) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QTreeWidgetItem4fontEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QFont(self->font(column));
}

//  void QTreeWidgetItem::setFont(int column, const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem7setFontEiRK5QFont(
    QTreeWidgetItem *self,
    int column,
    const QFont *font) {
  self->setFont(column, *font);
}

//  int QTreeWidgetItem::textAlignment(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTreeWidgetItem13textAlignmentEi(
    const QTreeWidgetItem *self,
    int column) {
  return self->textAlignment(column);
}

//  void QTreeWidgetItem::setTextAlignment(int column, int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem16setTextAlignmentEii(
    QTreeWidgetItem *self,
    int column,
    int alignment) {
  self->setTextAlignment(column, alignment);
}

//  void QTreeWidgetItem::setTextAlignment(int column, Qt::AlignmentFlag
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem16setTextAlignmentEiN2Qt13AlignmentFlagE(
    QTreeWidgetItem *self,
    int column,
    Qt::AlignmentFlag alignment) {
  self->setTextAlignment(column, alignment);
}

//  void QTreeWidgetItem::setTextAlignment(int column, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem16setTextAlignmentEi6QFlagsIN2Qt13AlignmentFlagEE(
    QTreeWidgetItem *self,
    int column,
    int alignment) {
  self->setTextAlignment(
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QBrush QTreeWidgetItem::background(int column) const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK15QTreeWidgetItem10backgroundEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QBrush(self->background(column));
}

//  void QTreeWidgetItem::setBackground(int column, const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem13setBackgroundEiRK6QBrush(
    QTreeWidgetItem *self,
    int column,
    const QBrush *brush) {
  self->setBackground(column, *brush);
}

//  QBrush QTreeWidgetItem::foreground(int column) const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK15QTreeWidgetItem10foregroundEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QBrush(self->foreground(column));
}

//  void QTreeWidgetItem::setForeground(int column, const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem13setForegroundEiRK6QBrush(
    QTreeWidgetItem *self,
    int column,
    const QBrush *brush) {
  self->setForeground(column, *brush);
}

//  Qt::CheckState QTreeWidgetItem::checkState(int column) const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK15QTreeWidgetItem10checkStateEi(
    const QTreeWidgetItem *self,
    int column) {
  return self->checkState(column);
}

//  void QTreeWidgetItem::setCheckState(int column, Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem13setCheckStateEiN2Qt10CheckStateE(
    QTreeWidgetItem *self,
    int column,
    Qt::CheckState state) {
  self->setCheckState(column, state);
}

//  QSize QTreeWidgetItem::sizeHint(int column) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QTreeWidgetItem8sizeHintEi(
    const QTreeWidgetItem *self,
    int column) {
  return new QSize(self->sizeHint(column));
}

//  void QTreeWidgetItem::setSizeHint(int column, const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem11setSizeHintEiRK5QSize(
    QTreeWidgetItem *self,
    int column,
    const QSize *size) {
  self->setSizeHint(column, *size);
}

//  QVariant QTreeWidgetItem::data(int column, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QTreeWidgetItem4dataEii(
    const QTreeWidgetItem *self,
    int column,
    int role) {
  return new QVariant(self->data(column, role));
}

//  void QTreeWidgetItem::setData(int column, int role, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem7setDataEiiRK8QVariant(
    QTreeWidgetItem *self,
    int column,
    int role,
    const QVariant *value) {
  self->setData(column, role, *value);
}

//  bool QTreeWidgetItem::operator<(const QTreeWidgetItem &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTreeWidgetItemltERKS_(
    const QTreeWidgetItem *self,
    const QTreeWidgetItem *other) {
  return self->operator<(*other);
}

//  QTreeWidgetItem *QTreeWidgetItem::parent() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK15QTreeWidgetItem6parentEv(
    const QTreeWidgetItem *self) {
  return self->parent();
}

//  QTreeWidgetItem *QTreeWidgetItem::child(int index) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK15QTreeWidgetItem5childEi(
    const QTreeWidgetItem *self,
    int index) {
  return self->child(index);
}

//  int QTreeWidgetItem::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTreeWidgetItem10childCountEv(const QTreeWidgetItem *self) {
  return self->childCount();
}

//  int QTreeWidgetItem::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTreeWidgetItem11columnCountEv(const QTreeWidgetItem *self) {
  return self->columnCount();
}

//  int QTreeWidgetItem::indexOfChild(QTreeWidgetItem *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTreeWidgetItem12indexOfChildEPS_(
    const QTreeWidgetItem *self,
    QTreeWidgetItem *child) {
  return self->indexOfChild(child);
}

//  void QTreeWidgetItem::addChild(QTreeWidgetItem *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem8addChildEPS_(
    QTreeWidgetItem *self,
    QTreeWidgetItem *child) {
  self->addChild(child);
}

//  void QTreeWidgetItem::insertChild(int index, QTreeWidgetItem *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem11insertChildEiPS_(
    QTreeWidgetItem *self,
    int index,
    QTreeWidgetItem *child) {
  self->insertChild(index, child);
}

//  void QTreeWidgetItem::removeChild(QTreeWidgetItem *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem11removeChildEPS_(
    QTreeWidgetItem *self,
    QTreeWidgetItem *child) {
  self->removeChild(child);
}

//  QTreeWidgetItem *QTreeWidgetItem::takeChild(int index)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN15QTreeWidgetItem9takeChildEi(
    QTreeWidgetItem *self,
    int index) {
  return self->takeChild(index);
}

//  void QTreeWidgetItem::addChildren(const QList<QTreeWidgetItem *>
//      &children)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem11addChildrenERK5QListIPS_E(
    QTreeWidgetItem *self,
    const QList<QTreeWidgetItem *> *children) {
  self->addChildren(*children);
}

//  void QTreeWidgetItem::insertChildren(int index, const
//      QList<QTreeWidgetItem *> &children)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem14insertChildrenEiRK5QListIPS_E(
    QTreeWidgetItem *self,
    int index,
    const QList<QTreeWidgetItem *> *children) {
  self->insertChildren(index, *children);
}

//  QList<QTreeWidgetItem *> QTreeWidgetItem::takeChildren()
extern "C" Q_DECL_EXPORT
QList<QTreeWidgetItem *> *ritual_ZN15QTreeWidgetItem12takeChildrenEv(
    QTreeWidgetItem *self) {
  return new QList<QTreeWidgetItem *>(self->takeChildren());
}

//  int QTreeWidgetItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTreeWidgetItem4typeEv(const QTreeWidgetItem *self) {
  return self->type();
}

//  void QTreeWidgetItem::sortChildren(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTreeWidgetItem12sortChildrenEiN2Qt9SortOrderE(
    QTreeWidgetItem *self,
    int column,
    Qt::SortOrder order) {
  self->sortChildren(column, order);
}

//  a Python function taken by a CuteQTreeWidgetItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTreeWidgetItem(
    QTreeWidgetItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTreeWidgetItem *>(self)->take(key, call);
}

//  QTreeWidgetItem *QTreeWidgetItem::clone() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_own_ZNK15QTreeWidgetItem5cloneEv(
    const QTreeWidgetItem *self) {
  return self->QTreeWidgetItem::clone();
}

//  QVariant QTreeWidgetItem::data(int column, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK15QTreeWidgetItem4dataEii(
    const QTreeWidgetItem *self,
    int column,
    int role) {
  return new QVariant(self->QTreeWidgetItem::data(column, role));
}

//  void QTreeWidgetItem::setData(int column, int role, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QTreeWidgetItem7setDataEiiRK8QVariant(
    QTreeWidgetItem *self,
    int column,
    int role,
    const QVariant *value) {
  self->QTreeWidgetItem::setData(column, role, *value);
}

//  QList<QTreeWidgetItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<QTreeWidgetItem *> *ritual_list_make_QTreeWidgetItem_ptr() {
  return new QList<QTreeWidgetItem *>();
}

//  void QList<QTreeWidgetItem *>::append(const QTreeWidgetItem * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QTreeWidgetItem_ptr(
    QList<QTreeWidgetItem *> *self,
    QTreeWidgetItem *element) {
  self->append(element);
}

//  qsizetype QList<QTreeWidgetItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QTreeWidgetItem_ptr(
    const QList<QTreeWidgetItem *> *self) {
  return self->size();
}

//  const QTreeWidgetItem * &QList<QTreeWidgetItem *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_list_at_QTreeWidgetItem_ptr(
    const QList<QTreeWidgetItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QTreeWidgetItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QTreeWidgetItem_ptr(QList<QTreeWidgetItem *> *self) {
  delete self;
}
