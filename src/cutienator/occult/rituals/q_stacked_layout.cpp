//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstackedlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstackedlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QStackedLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QStackedLayout10metaObjectEv(
    const QStackedLayout *self) {
  return self->metaObject();
}

//  QString QStackedLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStackedLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStackedLayout::tr(s, c, n));
}

//  QStackedLayout::QStackedLayout()
extern "C" Q_DECL_EXPORT
QStackedLayout *ritual_ZN14QStackedLayoutC1Ev() {
  return new QStackedLayout();
}

//  QStackedLayout::QStackedLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QStackedLayout *ritual_ZN14QStackedLayoutC1EP7QWidget(QWidget *parent) {
  return new QStackedLayout(parent);
}

//  QStackedLayout::QStackedLayout(QLayout *parentLayout)
extern "C" Q_DECL_EXPORT
QStackedLayout *ritual_ZN14QStackedLayoutC1EP7QLayout(
    QLayout *parentLayout) {
  return new QStackedLayout(parentLayout);
}

//  QStackedLayout::~QStackedLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayoutD1Ev(QStackedLayout *self) {
  delete self;
}

//  int QStackedLayout::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedLayout9addWidgetEP7QWidget(
    QStackedLayout *self,
    QWidget *w) {
  return self->addWidget(w);
}

//  int QStackedLayout::insertWidget(int index, QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedLayout12insertWidgetEiP7QWidget(
    QStackedLayout *self,
    int index,
    QWidget *w) {
  return self->insertWidget(index, w);
}

//  QWidget *QStackedLayout::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedLayout13currentWidgetEv(
    const QStackedLayout *self) {
  return self->currentWidget();
}

//  int QStackedLayout::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedLayout12currentIndexEv(const QStackedLayout *self) {
  return self->currentIndex();
}

//  QWidget *QStackedLayout::widget(int a0) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedLayout6widgetEi(
    const QStackedLayout *self,
    int a0) {
  return self->widget(a0);
}

//  int QStackedLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedLayout5countEv(const QStackedLayout *self) {
  return self->count();
}

//  StackingMode QStackedLayout::stackingMode() const
extern "C" Q_DECL_EXPORT
QStackedLayout::StackingMode ritual_ZNK14QStackedLayout12stackingModeEv(
    const QStackedLayout *self) {
  return self->stackingMode();
}

//  void QStackedLayout::setStackingMode(StackingMode stackingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout15setStackingModeENS_12StackingModeE(
    QStackedLayout *self,
    QStackedLayout::StackingMode stackingMode) {
  self->setStackingMode(stackingMode);
}

//  void QStackedLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout7addItemEP11QLayoutItem(
    QStackedLayout *self,
    QLayoutItem *item) {
  self->addItem(item);
}

//  QSize QStackedLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QStackedLayout8sizeHintEv(const QStackedLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QStackedLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QStackedLayout11minimumSizeEv(
    const QStackedLayout *self) {
  return new QSize(self->minimumSize());
}

//  QLayoutItem *QStackedLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK14QStackedLayout6itemAtEi(
    const QStackedLayout *self,
    int a0) {
  return self->itemAt(a0);
}

//  QLayoutItem *QStackedLayout::takeAt(int a0)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN14QStackedLayout6takeAtEi(
    QStackedLayout *self,
    int a0) {
  return self->takeAt(a0);
}

//  void QStackedLayout::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout11setGeometryERK5QRect(
    QStackedLayout *self,
    const QRect *rect) {
  self->setGeometry(*rect);
}

//  bool QStackedLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QStackedLayout17hasHeightForWidthEv(
    const QStackedLayout *self) {
  return self->hasHeightForWidth();
}

//  int QStackedLayout::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedLayout14heightForWidthEi(
    const QStackedLayout *self,
    int width) {
  return self->heightForWidth(width);
}

//  void QStackedLayout::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout15setCurrentIndexEi(
    QStackedLayout *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QStackedLayout::setCurrentWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedLayout16setCurrentWidgetEP7QWidget(
    QStackedLayout *self,
    QWidget *w) {
  self->setCurrentWidget(w);
}
