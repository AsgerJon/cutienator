//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tableview)
#if QT_CONFIG(tableview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSpanCollection::Span::Span()
extern "C" Q_DECL_EXPORT
QSpanCollection::Span *ritual_ZN15QSpanCollection4SpanC1Ev() {
  return new QSpanCollection::Span();
}

//  QSpanCollection::Span::Span(int row, int column, int rowCount, int
//      columnCount)
extern "C" Q_DECL_EXPORT
QSpanCollection::Span *ritual_ZN15QSpanCollection4SpanC1Eiiii(
    int row,
    int column,
    int rowCount,
    int columnCount) {
  return new QSpanCollection::Span(row, column, rowCount, columnCount);
}

//  int QSpanCollection::Span::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSpanCollection4Span3topEv(
    const QSpanCollection::Span *self) {
  return self->top();
}

//  int QSpanCollection::Span::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSpanCollection4Span4leftEv(
    const QSpanCollection::Span *self) {
  return self->left();
}

//  int QSpanCollection::Span::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSpanCollection4Span6bottomEv(
    const QSpanCollection::Span *self) {
  return self->bottom();
}

//  int QSpanCollection::Span::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSpanCollection4Span5rightEv(
    const QSpanCollection::Span *self) {
  return self->right();
}

//  int QSpanCollection::Span::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSpanCollection4Span6heightEv(
    const QSpanCollection::Span *self) {
  return self->height();
}

//  int QSpanCollection::Span::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSpanCollection4Span5widthEv(
    const QSpanCollection::Span *self) {
  return self->width();
}

//  QSpanCollection::Span::~Span()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection4SpanD1Ev(QSpanCollection::Span *self) {
  delete self;
}

#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(tableview)
