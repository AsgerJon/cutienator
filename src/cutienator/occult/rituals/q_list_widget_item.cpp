//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlistwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlistwidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qfont.h>
#include <QtGui/qbrush.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>

//  QListWidgetItem::QListWidgetItem(QListWidget *listview, int type)
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZN15QListWidgetItemC1EP11QListWidgeti(
    QListWidget *listview,
    int type) {
  return new QListWidgetItem(listview, type);
}

//  QListWidgetItem::QListWidgetItem(const QString &text, QListWidget
//      *listview, int type)
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZN15QListWidgetItemC1ERK7QStringP11QListWidgeti(
    const QString *text,
    QListWidget *listview,
    int type) {
  return new QListWidgetItem(*text, listview, type);
}

//  QListWidgetItem::QListWidgetItem(const QIcon &icon, const QString &text,
//      QListWidget *listview, int type)
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZN15QListWidgetItemC1ERK5QIconRK7QStringP11QListWidgeti(
    const QIcon *icon,
    const QString *text,
    QListWidget *listview,
    int type) {
  return new QListWidgetItem(*icon, *text, listview, type);
}

//  QListWidgetItem::QListWidgetItem(const QListWidgetItem &other)
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZN15QListWidgetItemC1ERKS_(
    const QListWidgetItem *other) {
  return new QListWidgetItem(*other);
}

//  QListWidgetItem::~QListWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItemD1Ev(QListWidgetItem *self) {
  delete self;
}

//  QListWidgetItem *QListWidgetItem::clone() const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK15QListWidgetItem5cloneEv(
    const QListWidgetItem *self) {
  return self->clone();
}

//  QListWidget *QListWidgetItem::listWidget() const
extern "C" Q_DECL_EXPORT
QListWidget *ritual_ZNK15QListWidgetItem10listWidgetEv(
    const QListWidgetItem *self) {
  return self->listWidget();
}

//  void QListWidgetItem::setSelected(bool select)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem11setSelectedEb(
    QListWidgetItem *self,
    bool select) {
  self->setSelected(select);
}

//  bool QListWidgetItem::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QListWidgetItem10isSelectedEv(const QListWidgetItem *self) {
  return self->isSelected();
}

//  void QListWidgetItem::setHidden(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem9setHiddenEb(
    QListWidgetItem *self,
    bool hide) {
  self->setHidden(hide);
}

//  bool QListWidgetItem::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QListWidgetItem8isHiddenEv(const QListWidgetItem *self) {
  return self->isHidden();
}

//  Qt::ItemFlags QListWidgetItem::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QListWidgetItem5flagsEv(const QListWidgetItem *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QListWidgetItem::setFlags(Qt::ItemFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE(
    QListWidgetItem *self,
    int flags) {
  self->setFlags(QFlags<Qt::ItemFlag>::fromInt(flags));
}

//  QString QListWidgetItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QListWidgetItem4textEv(const QListWidgetItem *self) {
  return new QString(self->text());
}

//  void QListWidgetItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem7setTextERK7QString(
    QListWidgetItem *self,
    const QString *text) {
  self->setText(*text);
}

//  QIcon QListWidgetItem::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK15QListWidgetItem4iconEv(const QListWidgetItem *self) {
  return new QIcon(self->icon());
}

//  void QListWidgetItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem7setIconERK5QIcon(
    QListWidgetItem *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  QString QListWidgetItem::statusTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QListWidgetItem9statusTipEv(
    const QListWidgetItem *self) {
  return new QString(self->statusTip());
}

//  void QListWidgetItem::setStatusTip(const QString &statusTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem12setStatusTipERK7QString(
    QListWidgetItem *self,
    const QString *statusTip) {
  self->setStatusTip(*statusTip);
}

//  QString QListWidgetItem::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QListWidgetItem7toolTipEv(const QListWidgetItem *self) {
  return new QString(self->toolTip());
}

//  void QListWidgetItem::setToolTip(const QString &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem10setToolTipERK7QString(
    QListWidgetItem *self,
    const QString *toolTip) {
  self->setToolTip(*toolTip);
}

//  QString QListWidgetItem::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QListWidgetItem9whatsThisEv(
    const QListWidgetItem *self) {
  return new QString(self->whatsThis());
}

//  void QListWidgetItem::setWhatsThis(const QString &whatsThis)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem12setWhatsThisERK7QString(
    QListWidgetItem *self,
    const QString *whatsThis) {
  self->setWhatsThis(*whatsThis);
}

//  QFont QListWidgetItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QListWidgetItem4fontEv(const QListWidgetItem *self) {
  return new QFont(self->font());
}

//  void QListWidgetItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem7setFontERK5QFont(
    QListWidgetItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  int QListWidgetItem::textAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QListWidgetItem13textAlignmentEv(
    const QListWidgetItem *self) {
  return self->textAlignment();
}

//  void QListWidgetItem::setTextAlignment(int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem16setTextAlignmentEi(
    QListWidgetItem *self,
    int alignment) {
  self->setTextAlignment(alignment);
}

//  void QListWidgetItem::setTextAlignment(Qt::AlignmentFlag alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem16setTextAlignmentEN2Qt13AlignmentFlagE(
    QListWidgetItem *self,
    Qt::AlignmentFlag alignment) {
  self->setTextAlignment(alignment);
}

//  void QListWidgetItem::setTextAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem16setTextAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QListWidgetItem *self,
    int alignment) {
  self->setTextAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QBrush QListWidgetItem::background() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK15QListWidgetItem10backgroundEv(
    const QListWidgetItem *self) {
  return new QBrush(self->background());
}

//  void QListWidgetItem::setBackground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem13setBackgroundERK6QBrush(
    QListWidgetItem *self,
    const QBrush *brush) {
  self->setBackground(*brush);
}

//  QBrush QListWidgetItem::foreground() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK15QListWidgetItem10foregroundEv(
    const QListWidgetItem *self) {
  return new QBrush(self->foreground());
}

//  void QListWidgetItem::setForeground(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem13setForegroundERK6QBrush(
    QListWidgetItem *self,
    const QBrush *brush) {
  self->setForeground(*brush);
}

//  Qt::CheckState QListWidgetItem::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK15QListWidgetItem10checkStateEv(
    const QListWidgetItem *self) {
  return self->checkState();
}

//  void QListWidgetItem::setCheckState(Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem13setCheckStateEN2Qt10CheckStateE(
    QListWidgetItem *self,
    Qt::CheckState state) {
  self->setCheckState(state);
}

//  QSize QListWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QListWidgetItem8sizeHintEv(const QListWidgetItem *self) {
  return new QSize(self->sizeHint());
}

//  void QListWidgetItem::setSizeHint(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem11setSizeHintERK5QSize(
    QListWidgetItem *self,
    const QSize *size) {
  self->setSizeHint(*size);
}

//  QVariant QListWidgetItem::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QListWidgetItem4dataEi(
    const QListWidgetItem *self,
    int role) {
  return new QVariant(self->data(role));
}

//  void QListWidgetItem::setData(int role, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QListWidgetItem7setDataEiRK8QVariant(
    QListWidgetItem *self,
    int role,
    const QVariant *value) {
  self->setData(role, *value);
}

//  bool QListWidgetItem::operator<(const QListWidgetItem &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QListWidgetItemltERKS_(
    const QListWidgetItem *self,
    const QListWidgetItem *other) {
  return self->operator<(*other);
}

//  int QListWidgetItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QListWidgetItem4typeEv(const QListWidgetItem *self) {
  return self->type();
}
