//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtablewidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qfont.h>
#include <QtGui/qbrush.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>

//  QTableWidgetItem::QTableWidgetItem(int type)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1Ei(int type) {
  return new QTableWidgetItem(type);
}

//  QTableWidgetItem::QTableWidgetItem(const QString &text, int type)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1ERK7QStringi(
    const QString *text,
    int type) {
  return new QTableWidgetItem(*text, type);
}

//  QTableWidgetItem::QTableWidgetItem(const QIcon &icon, const QString
//      &text, int type)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1ERK5QIconRK7QStringi(
    const QIcon *icon,
    const QString *text,
    int type) {
  return new QTableWidgetItem(*icon, *text, type);
}

//  QTableWidgetItem::QTableWidgetItem(const QTableWidgetItem &other)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN16QTableWidgetItemC1ERKS_(
    const QTableWidgetItem *other) {
  return new QTableWidgetItem(*other);
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
