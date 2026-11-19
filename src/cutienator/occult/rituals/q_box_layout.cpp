//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qboxlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QBoxLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QBoxLayout10metaObjectEv(
    const QBoxLayout *self) {
  return self->metaObject();
}

//  QString QBoxLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QBoxLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxLayout::tr(s, c, n));
}

//  QBoxLayout::QBoxLayout(Direction a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QBoxLayout *ritual_ZN10QBoxLayoutC1ENS_9DirectionEP7QWidget(
    QBoxLayout::Direction a0,
    QWidget *parent) {
  return new QBoxLayout(a0, parent);
}

//  QBoxLayout::~QBoxLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayoutD1Ev(QBoxLayout *self) {
  delete self;
}

//  Direction QBoxLayout::direction() const
extern "C" Q_DECL_EXPORT
QBoxLayout::Direction ritual_ZNK10QBoxLayout9directionEv(
    const QBoxLayout *self) {
  return self->direction();
}

//  void QBoxLayout::setDirection(Direction a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout12setDirectionENS_9DirectionE(
    QBoxLayout *self,
    QBoxLayout::Direction a0) {
  self->setDirection(a0);
}

//  void QBoxLayout::addSpacing(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10addSpacingEi(QBoxLayout *self, int size) {
  self->addSpacing(size);
}

//  void QBoxLayout::addStretch(int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10addStretchEi(QBoxLayout *self, int stretch) {
  self->addStretch(stretch);
}

//  void QBoxLayout::addSpacerItem(QSpacerItem *spacerItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout13addSpacerItemEP11QSpacerItem(
    QBoxLayout *self,
    QSpacerItem *spacerItem) {
  self->addSpacerItem(spacerItem);
}

//  void QBoxLayout::addWidget(QWidget *a0, int stretch, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout9addWidgetEP7QWidgeti6QFlagsIN2Qt13AlignmentFlagEE(
    QBoxLayout *self,
    QWidget *a0,
    int stretch,
    int alignment) {
  self->addWidget(
      a0,
      stretch,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QBoxLayout::addLayout(QLayout *layout, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout9addLayoutEP7QLayouti(
    QBoxLayout *self,
    QLayout *layout,
    int stretch) {
  self->addLayout(layout, stretch);
}

//  void QBoxLayout::addStrut(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout8addStrutEi(QBoxLayout *self, int a0) {
  self->addStrut(a0);
}

//  void QBoxLayout::addItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout7addItemEP11QLayoutItem(
    QBoxLayout *self,
    QLayoutItem *a0) {
  self->addItem(a0);
}

//  void QBoxLayout::insertSpacing(int index, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout13insertSpacingEii(
    QBoxLayout *self,
    int index,
    int size) {
  self->insertSpacing(index, size);
}

//  void QBoxLayout::insertStretch(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout13insertStretchEii(
    QBoxLayout *self,
    int index,
    int stretch) {
  self->insertStretch(index, stretch);
}

//  void QBoxLayout::insertSpacerItem(int index, QSpacerItem *spacerItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout16insertSpacerItemEiP11QSpacerItem(
    QBoxLayout *self,
    int index,
    QSpacerItem *spacerItem) {
  self->insertSpacerItem(index, spacerItem);
}

//  void QBoxLayout::insertWidget(int index, QWidget *widget, int stretch,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout12insertWidgetEiP7QWidgeti6QFlagsIN2Qt13AlignmentFlagEE(
    QBoxLayout *self,
    int index,
    QWidget *widget,
    int stretch,
    int alignment) {
  self->insertWidget(
      index,
      widget,
      stretch,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QBoxLayout::insertLayout(int index, QLayout *layout, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout12insertLayoutEiP7QLayouti(
    QBoxLayout *self,
    int index,
    QLayout *layout,
    int stretch) {
  self->insertLayout(index, layout, stretch);
}

//  void QBoxLayout::insertItem(int index, QLayoutItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10insertItemEiP11QLayoutItem(
    QBoxLayout *self,
    int index,
    QLayoutItem *a1) {
  self->insertItem(index, a1);
}

//  int QBoxLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout7spacingEv(const QBoxLayout *self) {
  return self->spacing();
}

//  void QBoxLayout::setSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10setSpacingEi(QBoxLayout *self, int spacing) {
  self->setSpacing(spacing);
}

//  bool QBoxLayout::setStretchFactor(QWidget *w, int stretch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBoxLayout16setStretchFactorEP7QWidgeti(
    QBoxLayout *self,
    QWidget *w,
    int stretch) {
  return self->setStretchFactor(w, stretch);
}

//  bool QBoxLayout::setStretchFactor(QLayout *l, int stretch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBoxLayout16setStretchFactorEP7QLayouti(
    QBoxLayout *self,
    QLayout *l,
    int stretch) {
  return self->setStretchFactor(l, stretch);
}

//  void QBoxLayout::setStretch(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10setStretchEii(
    QBoxLayout *self,
    int index,
    int stretch) {
  self->setStretch(index, stretch);
}

//  int QBoxLayout::stretch(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout7stretchEi(const QBoxLayout *self, int index) {
  return self->stretch(index);
}

//  QSize QBoxLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QBoxLayout8sizeHintEv(const QBoxLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QBoxLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QBoxLayout11minimumSizeEv(const QBoxLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QBoxLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QBoxLayout11maximumSizeEv(const QBoxLayout *self) {
  return new QSize(self->maximumSize());
}

//  bool QBoxLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QBoxLayout17hasHeightForWidthEv(const QBoxLayout *self) {
  return self->hasHeightForWidth();
}

//  int QBoxLayout::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout14heightForWidthEi(
    const QBoxLayout *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QBoxLayout::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout21minimumHeightForWidthEi(
    const QBoxLayout *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  Qt::Orientations QBoxLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout19expandingDirectionsEv(const QBoxLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QBoxLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout10invalidateEv(QBoxLayout *self) {
  self->invalidate();
}

//  QLayoutItem *QBoxLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK10QBoxLayout6itemAtEi(
    const QBoxLayout *self,
    int a0) {
  return self->itemAt(a0);
}

//  QLayoutItem *QBoxLayout::takeAt(int a0)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN10QBoxLayout6takeAtEi(QBoxLayout *self, int a0) {
  return self->takeAt(a0);
}

//  int QBoxLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBoxLayout5countEv(const QBoxLayout *self) {
  return self->count();
}

//  void QBoxLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBoxLayout11setGeometryERK5QRect(
    QBoxLayout *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}
