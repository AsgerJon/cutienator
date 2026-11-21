//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>

//  QWidgetItemV2::QWidgetItemV2(QWidget *widget)
extern "C" Q_DECL_EXPORT
QWidgetItemV2 *ritual_ZN13QWidgetItemV2C1EP7QWidget(QWidget *widget) {
  return new QWidgetItemV2(widget);
}

//  QWidgetItemV2::~QWidgetItemV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetItemV2D1Ev(QWidgetItemV2 *self) {
  delete self;
}

//  QSize QWidgetItemV2::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QWidgetItemV28sizeHintEv(const QWidgetItemV2 *self) {
  return new QSize(self->sizeHint());
}

//  QSize QWidgetItemV2::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QWidgetItemV211minimumSizeEv(const QWidgetItemV2 *self) {
  return new QSize(self->minimumSize());
}

//  QSize QWidgetItemV2::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QWidgetItemV211maximumSizeEv(const QWidgetItemV2 *self) {
  return new QSize(self->maximumSize());
}

//  int QWidgetItemV2::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QWidgetItemV214heightForWidthEi(
    const QWidgetItemV2 *self,
    int width) {
  return self->heightForWidth(width);
}
