//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgridlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgridlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QGridLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QGridLayout10metaObjectEv(
    const QGridLayout *self) {
  return self->metaObject();
}

//  QString QGridLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QGridLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGridLayout::tr(s, c, n));
}

//  QGridLayout::QGridLayout(QWidget *parent)
extern "C" Q_DECL_EXPORT
QGridLayout *ritual_ZN11QGridLayoutC1EP7QWidget(QWidget *parent) {
  return new QGridLayout(parent);
}

//  QGridLayout::~QGridLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayoutD1Ev(QGridLayout *self) {
  delete self;
}

//  QSize QGridLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QGridLayout8sizeHintEv(const QGridLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QGridLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QGridLayout11minimumSizeEv(const QGridLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QGridLayout::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QGridLayout11maximumSizeEv(const QGridLayout *self) {
  return new QSize(self->maximumSize());
}

//  void QGridLayout::setHorizontalSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout20setHorizontalSpacingEi(
    QGridLayout *self,
    int spacing) {
  self->setHorizontalSpacing(spacing);
}

//  int QGridLayout::horizontalSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout17horizontalSpacingEv(const QGridLayout *self) {
  return self->horizontalSpacing();
}

//  void QGridLayout::setVerticalSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout18setVerticalSpacingEi(
    QGridLayout *self,
    int spacing) {
  self->setVerticalSpacing(spacing);
}

//  int QGridLayout::verticalSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout15verticalSpacingEv(const QGridLayout *self) {
  return self->verticalSpacing();
}

//  void QGridLayout::setSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout10setSpacingEi(QGridLayout *self, int spacing) {
  self->setSpacing(spacing);
}

//  int QGridLayout::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout7spacingEv(const QGridLayout *self) {
  return self->spacing();
}

//  void QGridLayout::setRowStretch(int row, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout13setRowStretchEii(
    QGridLayout *self,
    int row,
    int stretch) {
  self->setRowStretch(row, stretch);
}

//  void QGridLayout::setColumnStretch(int column, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout16setColumnStretchEii(
    QGridLayout *self,
    int column,
    int stretch) {
  self->setColumnStretch(column, stretch);
}

//  int QGridLayout::rowStretch(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout10rowStretchEi(const QGridLayout *self, int row) {
  return self->rowStretch(row);
}

//  int QGridLayout::columnStretch(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout13columnStretchEi(
    const QGridLayout *self,
    int column) {
  return self->columnStretch(column);
}

//  void QGridLayout::setRowMinimumHeight(int row, int minSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout19setRowMinimumHeightEii(
    QGridLayout *self,
    int row,
    int minSize) {
  self->setRowMinimumHeight(row, minSize);
}

//  void QGridLayout::setColumnMinimumWidth(int column, int minSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout21setColumnMinimumWidthEii(
    QGridLayout *self,
    int column,
    int minSize) {
  self->setColumnMinimumWidth(column, minSize);
}

//  int QGridLayout::rowMinimumHeight(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout16rowMinimumHeightEi(
    const QGridLayout *self,
    int row) {
  return self->rowMinimumHeight(row);
}

//  int QGridLayout::columnMinimumWidth(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout18columnMinimumWidthEi(
    const QGridLayout *self,
    int column) {
  return self->columnMinimumWidth(column);
}

//  int QGridLayout::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout11columnCountEv(const QGridLayout *self) {
  return self->columnCount();
}

//  int QGridLayout::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout8rowCountEv(const QGridLayout *self) {
  return self->rowCount();
}

//  QRect QGridLayout::cellRect(int row, int column) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QGridLayout8cellRectEii(
    const QGridLayout *self,
    int row,
    int column) {
  return new QRect(self->cellRect(row, column));
}

//  bool QGridLayout::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGridLayout17hasHeightForWidthEv(const QGridLayout *self) {
  return self->hasHeightForWidth();
}

//  int QGridLayout::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout14heightForWidthEi(
    const QGridLayout *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QGridLayout::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout21minimumHeightForWidthEi(
    const QGridLayout *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  Qt::Orientations QGridLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout19expandingDirectionsEv(const QGridLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QGridLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout10invalidateEv(QGridLayout *self) {
  self->invalidate();
}

//  void QGridLayout::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addWidgetEP7QWidget(
    QGridLayout *self,
    QWidget *w) {
  self->addWidget(w);
}

//  void QGridLayout::addWidget(QWidget *a0, int row, int column,
//      Qt::Alignment a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addWidgetEP7QWidgetii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QWidget *a0,
    int row,
    int column,
    int a3) {
  self->addWidget(a0, row, column, QFlags<Qt::AlignmentFlag>::fromInt(a3));
}

//  void QGridLayout::addWidget(QWidget *a0, int row, int column, int
//      rowSpan, int columnSpan, Qt::Alignment a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addWidgetEP7QWidgetiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QWidget *a0,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int a5) {
  self->addWidget(
      a0,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(a5));
}

//  void QGridLayout::addLayout(QLayout *a0, int row, int column,
//      Qt::Alignment a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addLayoutEP7QLayoutii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QLayout *a0,
    int row,
    int column,
    int a3) {
  self->addLayout(a0, row, column, QFlags<Qt::AlignmentFlag>::fromInt(a3));
}

//  void QGridLayout::addLayout(QLayout *a0, int row, int column, int
//      rowSpan, int columnSpan, Qt::Alignment a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout9addLayoutEP7QLayoutiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QLayout *a0,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int a5) {
  self->addLayout(
      a0,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(a5));
}

//  void QGridLayout::setOriginCorner(Qt::Corner a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout15setOriginCornerEN2Qt6CornerE(
    QGridLayout *self,
    Qt::Corner a0) {
  self->setOriginCorner(a0);
}

//  Qt::Corner QGridLayout::originCorner() const
extern "C" Q_DECL_EXPORT
Qt::Corner ritual_ZNK11QGridLayout12originCornerEv(const QGridLayout *self) {
  return self->originCorner();
}

//  QLayoutItem *QGridLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK11QGridLayout6itemAtEi(
    const QGridLayout *self,
    int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QGridLayout::itemAtPosition(int row, int column) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK11QGridLayout14itemAtPositionEii(
    const QGridLayout *self,
    int row,
    int column) {
  return self->itemAtPosition(row, column);
}

//  QLayoutItem *QGridLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN11QGridLayout6takeAtEi(QGridLayout *self, int index) {
  return self->takeAt(index);
}

//  int QGridLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QGridLayout5countEv(const QGridLayout *self) {
  return self->count();
}

//  void QGridLayout::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout11setGeometryERK5QRect(
    QGridLayout *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  void QGridLayout::addItem(QLayoutItem *item, int row, int column, int
//      rowSpan, int columnSpan, Qt::Alignment a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout7addItemEP11QLayoutItemiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayout *self,
    QLayoutItem *item,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int a5) {
  self->addItem(
      item,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(a5));
}

//  void QGridLayout::setDefaultPositioning(int n, Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGridLayout21setDefaultPositioningEiN2Qt11OrientationE(
    QGridLayout *self,
    int n,
    Qt::Orientation orient) {
  self->setDefaultPositioning(n, orient);
}

//  void QGridLayout::getItemPosition(int idx, int *row, int *column, int
//      *rowSpan, int *columnSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QGridLayout15getItemPositionEiPiS0_S0_S0_(
    const QGridLayout *self,
    int idx,
    int *row,
    int *column,
    int *rowSpan,
    int *columnSpan) {
  self->getItemPosition(idx, row, column, rowSpan, columnSpan);
}
