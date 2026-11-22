//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtoolbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtoolbox.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>

//  const QMetaObject *QToolBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QToolBox10metaObjectEv(const QToolBox *self) {
  return self->metaObject();
}

//  QString QToolBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QToolBox2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QToolBox::tr(s, c, n));
}

//  QToolBox::QToolBox(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QToolBox *ritual_ZN8QToolBoxC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new QToolBox(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QToolBox::~QToolBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBoxD1Ev(QToolBox *self) {
  delete self;
}

//  int QToolBox::addItem(QWidget *widget, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox7addItemEP7QWidgetRK7QString(
    QToolBox *self,
    QWidget *widget,
    const QString *text) {
  return self->addItem(widget, *text);
}

//  int QToolBox::addItem(QWidget *widget, const QIcon &icon, const QString
//      &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox7addItemEP7QWidgetRK5QIconRK7QString(
    QToolBox *self,
    QWidget *widget,
    const QIcon *icon,
    const QString *text) {
  return self->addItem(widget, *icon, *text);
}

//  int QToolBox::insertItem(int index, QWidget *widget, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox10insertItemEiP7QWidgetRK7QString(
    QToolBox *self,
    int index,
    QWidget *widget,
    const QString *text) {
  return self->insertItem(index, widget, *text);
}

//  int QToolBox::insertItem(int index, QWidget *widget, const QIcon &icon,
//      const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QToolBox10insertItemEiP7QWidgetRK5QIconRK7QString(
    QToolBox *self,
    int index,
    QWidget *widget,
    const QIcon *icon,
    const QString *text) {
  return self->insertItem(index, widget, *icon, *text);
}

//  void QToolBox::removeItem(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox10removeItemEi(QToolBox *self, int index) {
  self->removeItem(index);
}

//  void QToolBox::setItemEnabled(int index, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox14setItemEnabledEib(
    QToolBox *self,
    int index,
    bool enabled) {
  self->setItemEnabled(index, enabled);
}

//  bool QToolBox::isItemEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBox13isItemEnabledEi(const QToolBox *self, int index) {
  return self->isItemEnabled(index);
}

//  void QToolBox::setItemText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox11setItemTextEiRK7QString(
    QToolBox *self,
    int index,
    const QString *text) {
  self->setItemText(index, *text);
}

//  QString QToolBox::itemText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QToolBox8itemTextEi(const QToolBox *self, int index) {
  return new QString(self->itemText(index));
}

//  void QToolBox::setItemIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox11setItemIconEiRK5QIcon(
    QToolBox *self,
    int index,
    const QIcon *icon) {
  self->setItemIcon(index, *icon);
}

//  QIcon QToolBox::itemIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK8QToolBox8itemIconEi(const QToolBox *self, int index) {
  return new QIcon(self->itemIcon(index));
}

//  void QToolBox::setItemToolTip(int index, const QString &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox14setItemToolTipEiRK7QString(
    QToolBox *self,
    int index,
    const QString *toolTip) {
  self->setItemToolTip(index, *toolTip);
}

//  QString QToolBox::itemToolTip(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QToolBox11itemToolTipEi(
    const QToolBox *self,
    int index) {
  return new QString(self->itemToolTip(index));
}

//  int QToolBox::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBox12currentIndexEv(const QToolBox *self) {
  return self->currentIndex();
}

//  QWidget *QToolBox::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QToolBox13currentWidgetEv(const QToolBox *self) {
  return self->currentWidget();
}

//  QWidget *QToolBox::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QToolBox6widgetEi(const QToolBox *self, int index) {
  return self->widget(index);
}

//  int QToolBox::indexOf(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBox7indexOfEPK7QWidget(
    const QToolBox *self,
    const QWidget *widget) {
  return self->indexOf(widget);
}

//  int QToolBox::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBox5countEv(const QToolBox *self) {
  return self->count();
}

//  void QToolBox::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox15setCurrentIndexEi(QToolBox *self, int index) {
  self->setCurrentIndex(index);
}

//  void QToolBox::setCurrentWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBox16setCurrentWidgetEP7QWidget(
    QToolBox *self,
    QWidget *widget) {
  self->setCurrentWidget(widget);
}
