//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtablewidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qfont.h>
#include <QtGui/qbrush.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QTableWidgetItem that Python can take functions over in. Every QTableWidgetItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQTableWidgetItemCall0)(const void *, int *);
typedef const QVariant * (*CuteQTableWidgetItemCall1)(const void *, int, int *);
typedef void (*CuteQTableWidgetItemCall2)(const void *, int, const QVariant *, int *);
class CuteQTableWidgetItem : public QTableWidgetItem {
public:
  using QTableWidgetItem::QTableWidgetItem;
  CuteQTableWidgetItem(const QTableWidgetItem &other) : QTableWidgetItem(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QTableWidgetItem5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QTableWidgetItem4dataEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QTableWidgetItem7setDataEiRK8QVariant")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QTableWidgetItem *QTableWidgetItem::clone() const
  QTableWidgetItem *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTableWidgetItemCall0 call = reinterpret_cast<CuteQTableWidgetItemCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTableWidgetItem *>(given);
    }
    return QTableWidgetItem::clone();
  }

  //  QVariant QTableWidgetItem::data(int role) const
  QVariant data(int role) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTableWidgetItemCall1 call = reinterpret_cast<CuteQTableWidgetItemCall1>(taken[1]);
      const QVariant * given = call(this, role, &handled);
      if (handled && given) return *given;
    }
    return QTableWidgetItem::data(role);
  }

  //  void QTableWidgetItem::setData(int role, const QVariant &value)
  void setData(int role, const QVariant &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTableWidgetItemCall2 call = reinterpret_cast<CuteQTableWidgetItemCall2>(taken[2]);
      call(this, role, &value, &handled);
      if (handled) return;
    }
    QTableWidgetItem::setData(role, value);
  }
};

//  QTableWidgetItem::QTableWidgetItem(int type)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1Ei(int type) {
  return new CuteQTableWidgetItem(type);
}

//  QTableWidgetItem::QTableWidgetItem(const QString &text, int type)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1ERK7QStringi(
    const QString *text,
    int type) {
  return new CuteQTableWidgetItem(*text, type);
}

//  QTableWidgetItem::QTableWidgetItem(const QIcon &icon, const QString
//      &text, int type)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1ERK5QIconRK7QStringi(
    const QIcon *icon,
    const QString *text,
    int type) {
  return new CuteQTableWidgetItem(*icon, *text, type);
}

//  QTableWidgetItem::QTableWidgetItem(const QTableWidgetItem &other)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1ERKS_(
    const QTableWidgetItem *other) {
  return new CuteQTableWidgetItem(*other);
}

//  QTableWidgetItem::~QTableWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItemD1Ev(QTableWidgetItem *self) {
  delete self;
}

//  QTableWidgetItem *QTableWidgetItem::clone() const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK16QTableWidgetItem5cloneEv(
    const QTableWidgetItem *self) {
  return self->clone();
}

//  QTableWidget *QTableWidgetItem::tableWidget() const
extern "C" Q_DECL_EXPORT
QTableWidget *ritual_ZNK16QTableWidgetItem11tableWidgetEv(
    const QTableWidgetItem *self) {
  return self->tableWidget();
}

//  int QTableWidgetItem::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTableWidgetItem3rowEv(const QTableWidgetItem *self) {
  return self->row();
}

//  int QTableWidgetItem::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTableWidgetItem6columnEv(const QTableWidgetItem *self) {
  return self->column();
}

//  void QTableWidgetItem::setSelected(bool select)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem11setSelectedEb(
    QTableWidgetItem *self,
    bool select) {
  self->setSelected(select);
}

//  bool QTableWidgetItem::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTableWidgetItem10isSelectedEv(
    const QTableWidgetItem *self) {
  return self->isSelected();
}

//  Qt::ItemFlags QTableWidgetItem::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTableWidgetItem5flagsEv(const QTableWidgetItem *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QTableWidgetItem::setFlags(Qt::ItemFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE(
    QTableWidgetItem *self,
    int flags) {
  self->setFlags(QFlags<Qt::ItemFlag>::fromInt(flags));
}

//  QString QTableWidgetItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTableWidgetItem4textEv(const QTableWidgetItem *self) {
  return new QString(self->text());
}

//  void QTableWidgetItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem7setTextERK7QString(
    QTableWidgetItem *self,
    const QString *text) {
  self->setText(*text);
}

//  QIcon QTableWidgetItem::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK16QTableWidgetItem4iconEv(const QTableWidgetItem *self) {
  return new QIcon(self->icon());
}

//  void QTableWidgetItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem7setIconERK5QIcon(
    QTableWidgetItem *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  QString QTableWidgetItem::statusTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTableWidgetItem9statusTipEv(
    const QTableWidgetItem *self) {
  return new QString(self->statusTip());
}

//  void QTableWidgetItem::setStatusTip(const QString &statusTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem12setStatusTipERK7QString(
    QTableWidgetItem *self,
    const QString *statusTip) {
  self->setStatusTip(*statusTip);
}

//  QString QTableWidgetItem::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTableWidgetItem7toolTipEv(
    const QTableWidgetItem *self) {
  return new QString(self->toolTip());
}

//  void QTableWidgetItem::setToolTip(const QString &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem10setToolTipERK7QString(
    QTableWidgetItem *self,
    const QString *toolTip) {
  self->setToolTip(*toolTip);
}

//  QString QTableWidgetItem::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTableWidgetItem9whatsThisEv(
    const QTableWidgetItem *self) {
  return new QString(self->whatsThis());
}

//  void QTableWidgetItem::setWhatsThis(const QString &whatsThis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem12setWhatsThisERK7QString(
    QTableWidgetItem *self,
    const QString *whatsThis) {
  self->setWhatsThis(*whatsThis);
}

//  QFont QTableWidgetItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16QTableWidgetItem4fontEv(const QTableWidgetItem *self) {
  return new QFont(self->font());
}

//  void QTableWidgetItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem7setFontERK5QFont(
    QTableWidgetItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  int QTableWidgetItem::textAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTableWidgetItem13textAlignmentEv(
    const QTableWidgetItem *self) {
  return self->textAlignment();
}

//  void QTableWidgetItem::setTextAlignment(int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem16setTextAlignmentEi(
    QTableWidgetItem *self,
    int alignment) {
  self->setTextAlignment(alignment);
}

//  void QTableWidgetItem::setTextAlignment(Qt::AlignmentFlag alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem16setTextAlignmentEN2Qt13AlignmentFlagE(
    QTableWidgetItem *self,
    Qt::AlignmentFlag alignment) {
  self->setTextAlignment(alignment);
}

//  void QTableWidgetItem::setTextAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem16setTextAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QTableWidgetItem *self,
    int alignment) {
  self->setTextAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QBrush QTableWidgetItem::background() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK16QTableWidgetItem10backgroundEv(
    const QTableWidgetItem *self) {
  return new QBrush(self->background());
}

//  void QTableWidgetItem::setBackground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem13setBackgroundERK6QBrush(
    QTableWidgetItem *self,
    const QBrush *brush) {
  self->setBackground(*brush);
}

//  QBrush QTableWidgetItem::foreground() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK16QTableWidgetItem10foregroundEv(
    const QTableWidgetItem *self) {
  return new QBrush(self->foreground());
}

//  void QTableWidgetItem::setForeground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem13setForegroundERK6QBrush(
    QTableWidgetItem *self,
    const QBrush *brush) {
  self->setForeground(*brush);
}

//  Qt::CheckState QTableWidgetItem::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK16QTableWidgetItem10checkStateEv(
    const QTableWidgetItem *self) {
  return self->checkState();
}

//  void QTableWidgetItem::setCheckState(Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem13setCheckStateEN2Qt10CheckStateE(
    QTableWidgetItem *self,
    Qt::CheckState state) {
  self->setCheckState(state);
}

//  QSize QTableWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QTableWidgetItem8sizeHintEv(
    const QTableWidgetItem *self) {
  return new QSize(self->sizeHint());
}

//  void QTableWidgetItem::setSizeHint(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem11setSizeHintERK5QSize(
    QTableWidgetItem *self,
    const QSize *size) {
  self->setSizeHint(*size);
}

//  QVariant QTableWidgetItem::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QTableWidgetItem4dataEi(
    const QTableWidgetItem *self,
    int role) {
  return new QVariant(self->data(role));
}

//  void QTableWidgetItem::setData(int role, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTableWidgetItem7setDataEiRK8QVariant(
    QTableWidgetItem *self,
    int role,
    const QVariant *value) {
  self->setData(role, *value);
}

//  bool QTableWidgetItem::operator<(const QTableWidgetItem &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTableWidgetItemltERKS_(
    const QTableWidgetItem *self,
    const QTableWidgetItem *other) {
  return self->operator<(*other);
}

//  int QTableWidgetItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTableWidgetItem4typeEv(const QTableWidgetItem *self) {
  return self->type();
}

//  a Python function taken by a CuteQTableWidgetItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTableWidgetItem(
    QTableWidgetItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTableWidgetItem *>(self)->take(key, call);
}

//  QTableWidgetItem *QTableWidgetItem::clone() const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_own_ZNK16QTableWidgetItem5cloneEv(
    const QTableWidgetItem *self) {
  return self->QTableWidgetItem::clone();
}

//  QVariant QTableWidgetItem::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QTableWidgetItem4dataEi(
    const QTableWidgetItem *self,
    int role) {
  return new QVariant(self->QTableWidgetItem::data(role));
}

//  void QTableWidgetItem::setData(int role, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QTableWidgetItem7setDataEiRK8QVariant(
    QTableWidgetItem *self,
    int role,
    const QVariant *value) {
  self->QTableWidgetItem::setData(role, *value);
}

//  QList<QTableWidgetItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<QTableWidgetItem *> *ritual_list_make_QTableWidgetItem_ptr() {
  return new QList<QTableWidgetItem *>();
}

//  void QList<QTableWidgetItem *>::append(const QTableWidgetItem * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QTableWidgetItem_ptr(
    QList<QTableWidgetItem *> *self,
    QTableWidgetItem *element) {
  self->append(element);
}

//  qsizetype QList<QTableWidgetItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QTableWidgetItem_ptr(
    const QList<QTableWidgetItem *> *self) {
  return self->size();
}

//  const QTableWidgetItem * &QList<QTableWidgetItem *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_list_at_QTableWidgetItem_ptr(
    const QList<QTableWidgetItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QTableWidgetItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QTableWidgetItem_ptr(QList<QTableWidgetItem *> *self) {
  delete self;
}
