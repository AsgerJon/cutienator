//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qmargins.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QLayout10metaObjectEv(const QLayout *self) {
  return self->metaObject();
}

//  QString QLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLayout2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QLayout::tr(s, c, n));
}

//  QLayout::~QLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayoutD1Ev(QLayout *self) {
  delete self;
}

//  int QLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout7spacingEv(const QLayout *self) {
  return self->spacing();
}

//  void QLayout::setSpacing(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10setSpacingEi(QLayout *self, int a0) {
  self->setSpacing(a0);
}

//  void QLayout::setContentsMargins(int left, int top, int right, int
//      bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout18setContentsMarginsEiiii(
    QLayout *self,
    int left,
    int top,
    int right,
    int bottom) {
  self->setContentsMargins(left, top, right, bottom);
}

//  void QLayout::setContentsMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout18setContentsMarginsERK8QMargins(
    QLayout *self,
    const QMargins *margins) {
  self->setContentsMargins(*margins);
}

//  void QLayout::unsetContentsMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout20unsetContentsMarginsEv(QLayout *self) {
  self->unsetContentsMargins();
}

//  void QLayout::getContentsMargins(int *left, int *top, int *right, int
//      *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QLayout18getContentsMarginsEPiS0_S0_S0_(
    const QLayout *self,
    int *left,
    int *top,
    int *right,
    int *bottom) {
  self->getContentsMargins(left, top, right, bottom);
}

//  QMargins QLayout::contentsMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK7QLayout15contentsMarginsEv(const QLayout *self) {
  return new QMargins(self->contentsMargins());
}

//  QRect QLayout::contentsRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QLayout12contentsRectEv(const QLayout *self) {
  return new QRect(self->contentsRect());
}

//  bool QLayout::setAlignment(QWidget *w, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLayout12setAlignmentEP7QWidget6QFlagsIN2Qt13AlignmentFlagEE(
    QLayout *self,
    QWidget *w,
    int alignment) {
  return self->setAlignment(
      w,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  bool QLayout::setAlignment(QLayout *l, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLayout12setAlignmentEPS_6QFlagsIN2Qt13AlignmentFlagEE(
    QLayout *self,
    QLayout *l,
    int alignment) {
  return self->setAlignment(
      l,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QLayout::setSizeConstraint(SizeConstraint constraint)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout17setSizeConstraintENS_14SizeConstraintE(
    QLayout *self,
    QLayout::SizeConstraint constraint) {
  self->setSizeConstraint(constraint);
}

//  SizeConstraint QLayout::sizeConstraint() const
extern "C" Q_DECL_EXPORT
QLayout::SizeConstraint ritual_ZNK7QLayout14sizeConstraintEv(
    const QLayout *self) {
  return self->sizeConstraint();
}

//  void QLayout::setSizeConstraints(SizeConstraint horizontal,
//      SizeConstraint vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout18setSizeConstraintsENS_14SizeConstraintES0_(
    QLayout *self,
    QLayout::SizeConstraint horizontal,
    QLayout::SizeConstraint vertical) {
  self->setSizeConstraints(horizontal, vertical);
}

//  void QLayout::setHorizontalSizeConstraint(SizeConstraint constraint)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout27setHorizontalSizeConstraintENS_14SizeConstraintE(
    QLayout *self,
    QLayout::SizeConstraint constraint) {
  self->setHorizontalSizeConstraint(constraint);
}

//  SizeConstraint QLayout::horizontalSizeConstraint() const
extern "C" Q_DECL_EXPORT
QLayout::SizeConstraint ritual_ZNK7QLayout24horizontalSizeConstraintEv(
    const QLayout *self) {
  return self->horizontalSizeConstraint();
}

//  void QLayout::setVerticalSizeConstraint(SizeConstraint constraint)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout25setVerticalSizeConstraintENS_14SizeConstraintE(
    QLayout *self,
    QLayout::SizeConstraint constraint) {
  self->setVerticalSizeConstraint(constraint);
}

//  SizeConstraint QLayout::verticalSizeConstraint() const
extern "C" Q_DECL_EXPORT
QLayout::SizeConstraint ritual_ZNK7QLayout22verticalSizeConstraintEv(
    const QLayout *self) {
  return self->verticalSizeConstraint();
}

//  void QLayout::setMenuBar(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10setMenuBarEP7QWidget(QLayout *self, QWidget *w) {
  self->setMenuBar(w);
}

//  QWidget *QLayout::menuBar() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QLayout7menuBarEv(const QLayout *self) {
  return self->menuBar();
}

//  QWidget *QLayout::parentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QLayout12parentWidgetEv(const QLayout *self) {
  return self->parentWidget();
}

//  void QLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10invalidateEv(QLayout *self) {
  self->invalidate();
}

//  QRect QLayout::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QLayout8geometryEv(const QLayout *self) {
  return new QRect(self->geometry());
}

//  bool QLayout::activate()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLayout8activateEv(QLayout *self) {
  return self->activate();
}

//  void QLayout::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout6updateEv(QLayout *self) {
  self->update();
}

//  void QLayout::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout9addWidgetEP7QWidget(QLayout *self, QWidget *w) {
  self->addWidget(w);
}

//  void QLayout::addItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout7addItemEP11QLayoutItem(
    QLayout *self,
    QLayoutItem *a0) {
  self->addItem(a0);
}

//  void QLayout::removeWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout12removeWidgetEP7QWidget(QLayout *self, QWidget *w) {
  self->removeWidget(w);
}

//  void QLayout::removeItem(QLayoutItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10removeItemEP11QLayoutItem(
    QLayout *self,
    QLayoutItem *a0) {
  self->removeItem(a0);
}

//  Qt::Orientations QLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout19expandingDirectionsEv(const QLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  QSize QLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout11minimumSizeEv(const QLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout11maximumSizeEv(const QLayout *self) {
  return new QSize(self->maximumSize());
}

//  void QLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout11setGeometryERK5QRect(
    QLayout *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QLayoutItem *QLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK7QLayout6itemAtEi(const QLayout *self, int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN7QLayout6takeAtEi(QLayout *self, int index) {
  return self->takeAt(index);
}

//  int QLayout::indexOf(const QWidget *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout7indexOfEPK7QWidget(
    const QLayout *self,
    const QWidget *a0) {
  return self->indexOf(a0);
}

//  int QLayout::indexOf(const QLayoutItem *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout7indexOfEPK11QLayoutItem(
    const QLayout *self,
    const QLayoutItem *a0) {
  return self->indexOf(a0);
}

//  int QLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout5countEv(const QLayout *self) {
  return self->count();
}

//  bool QLayout::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLayout7isEmptyEv(const QLayout *self) {
  return self->isEmpty();
}

//  QSizePolicy::ControlTypes QLayout::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout12controlTypesEv(const QLayout *self) {
  return static_cast<int>(self->controlTypes().toInt());
}

//  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
//      Qt::FindChildOptions options)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE(
    QLayout *self,
    QWidget *from,
    QWidget *to,
    int options) {
  return self->replaceWidget(
      from,
      to,
      QFlags<Qt::FindChildOption>::fromInt(options));
}

//  int QLayout::totalMinimumHeightForWidth(int w) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout26totalMinimumHeightForWidthEi(
    const QLayout *self,
    int w) {
  return self->totalMinimumHeightForWidth(w);
}

//  int QLayout::totalHeightForWidth(int w) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLayout19totalHeightForWidthEi(const QLayout *self, int w) {
  return self->totalHeightForWidth(w);
}

//  QSize QLayout::totalMinimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout16totalMinimumSizeEv(const QLayout *self) {
  return new QSize(self->totalMinimumSize());
}

//  QSize QLayout::totalMaximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout16totalMaximumSizeEv(const QLayout *self) {
  return new QSize(self->totalMaximumSize());
}

//  QSize QLayout::totalSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QLayout13totalSizeHintEv(const QLayout *self) {
  return new QSize(self->totalSizeHint());
}

//  QLayout *QLayout::layout()
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN7QLayout6layoutEv(QLayout *self) {
  return self->layout();
}

//  void QLayout::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLayout10setEnabledEb(QLayout *self, bool a0) {
  self->setEnabled(a0);
}

//  bool QLayout::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLayout9isEnabledEv(const QLayout *self) {
  return self->isEnabled();
}

//  QSize QLayout::closestAcceptableSize(const QWidget *w, const QSize &s)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN7QLayout21closestAcceptableSizeEPK7QWidgetRK5QSize(
    const QWidget *w,
    const QSize *s) {
  return new QSize(QLayout::closestAcceptableSize(w, *s));
}

//  QLayout as the QLayoutItem it is built on
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_cast_QLayout_QLayoutItem(QLayout *self) {
  return static_cast<QLayoutItem *>(self);
}
