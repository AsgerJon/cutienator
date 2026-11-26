//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qctextlayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qctextlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qfontmetrics.h>
#include <utility>
#include <QtCore/QRectF>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qctextlayout_p.h>
#include <QtGui/QTransform>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 11, as _ZN12QCTextLayout19convertToQtWrapModeEN14QCanvasPainter8WrapModeE
inline QTextOption::WrapMode QCTextLayout::convertToQtWrapMode(QCanvasPainter::WrapMode mode)
{
    switch (mode) {
    case QCanvasPainter::WrapMode::NoWrap:
        return QTextOption::NoWrap;
        break;
    case QCanvasPainter::WrapMode::Wrap:
        return QTextOption::WrapAtWordBoundaryOrAnywhere;
        break;
    case QCanvasPainter::WrapMode::WordWrap:
        return QTextOption::WordWrap;
        break;
    case QCanvasPainter::WrapMode::WrapAnywhere:
        return QTextOption::WrapAnywhere;
        break;
    }
    return QTextOption::NoWrap;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 30, as _ZN12QCTextLayout20convertToQtAlignmentEN14QCanvasPainter9TextAlignE
inline Qt::Alignment QCTextLayout::convertToQtAlignment(QCanvasPainter::TextAlign alignment)
{
    switch (alignment) {
    case QCanvasPainter::TextAlign::Left:
        return Qt::AlignLeft;
        break;
    case QCanvasPainter::TextAlign::Center:
        return Qt::AlignCenter;
        break;
    case QCanvasPainter::TextAlign::Right:
        return Qt::AlignRight;
        break;
    default:
        break;
    }
    return Qt::AlignLeft;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 48, as _ZN12QCTextLayout26calculateVerticalAlignmentEN14QCanvasPainter12TextBaselineERK6QRectFRK13QFontMetricsFS4_
inline float QCTextLayout::calculateVerticalAlignment(QCanvasPainter::TextBaseline baseline, const QRectF &rect,
                                               const QFontMetricsF &metrics, const QRectF &layoutRect)
{
    float offset = 0;
    switch (baseline) {
    case QCanvasPainter::TextBaseline::Top:
        break;
    case QCanvasPainter::TextBaseline::Hanging:
        offset = -metrics.height() + metrics.ascent();
        break;
    case QCanvasPainter::TextBaseline::Middle:
        offset = rect.height() * 0.5 - layoutRect.height() * 0.5;
        break;
    case QCanvasPainter::TextBaseline::Alphabetic:
        offset = rect.height() - layoutRect.height() + metrics.descent();
        break;
    case QCanvasPainter::TextBaseline::Bottom:
        offset = rect.height() - layoutRect.height();
        break;
    }

    return offset;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 72, as _ZN12QCTextLayout28calculateHorizontalAlignmentEN14QCanvasPainter9TextAlignERK6QRectFfS4_
inline std::pair<float, float> QCTextLayout::calculateHorizontalAlignment(QCanvasPainter::TextAlign align,
                                                                   const QRectF &rect,
                                                                   float layoutWidth,
                                                                   const QRectF &layoutRect)
{
    float offset1 = 0;
    float offset2 = 0;
    float paddingOffset = (layoutRect.width() - layoutWidth);
    float alignOffset = (rect.width() - layoutRect.width());
    switch (align) {
    case QCanvasPainter::TextAlign::Left:
        offset2 = -paddingOffset;
        break;
    case QCanvasPainter::TextAlign::Right:
        offset1 = paddingOffset + alignOffset;
        offset2 = alignOffset;
        break;
    case QCanvasPainter::TextAlign::Center:
        offset1 = (alignOffset + paddingOffset) * 0.5f;
        offset2 = (alignOffset - paddingOffset) * 0.5f;
        break;
    case QCanvasPainter::TextAlign::Start:
    case QCanvasPainter::TextAlign::End:
    default:
        break;
    }
    return { offset1, offset2 };
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 101, as _ZN12QCTextLayout20convertToQtDirectionEN14QCanvasPainter13TextDirectionE
inline Qt::LayoutDirection QCTextLayout::convertToQtDirection(QCanvasPainter::TextDirection direction)
{
    switch (direction) {
    case QCanvasPainter::TextDirection::LeftToRight:
        return Qt::LeftToRight;
    case QCanvasPainter::TextDirection::RightToLeft:
        return Qt::RightToLeft;
    case QCanvasPainter::TextDirection::Inherit:
        return QGuiApplication::layoutDirection();
    case QCanvasPainter::TextDirection::Auto:
        return Qt::LayoutDirectionAuto;
    }
    Q_UNREACHABLE_RETURN(Qt::LayoutDirectionAuto);
}
//  -----------------------------------------------------------------------

//  QTextOption::WrapMode
//      QCTextLayout::convertToQtWrapMode(QCanvasPainter::WrapMode mode)
extern "C" Q_DECL_EXPORT
QTextOption::WrapMode ritual_ZN12QCTextLayout19convertToQtWrapModeEN14QCanvasPainter8WrapModeE(
    QCanvasPainter::WrapMode mode) {
  return QCTextLayout::convertToQtWrapMode(mode);
}

//  Qt::Alignment
//      QCTextLayout::convertToQtAlignment(QCanvasPainter::TextAlign
//      alignment)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QCTextLayout20convertToQtAlignmentEN14QCanvasPainter9TextAlignE(
    QCanvasPainter::TextAlign alignment) {
  return static_cast<int>(
      QCTextLayout::convertToQtAlignment(
          alignment).toInt());
}

//  float
//      QCTextLayout::calculateVerticalAlignment(QCanvasPainter::TextBaseline
//      baseline, const QRectF &rect, const QFontMetricsF &metrics, const
//      QRectF &layoutRect)
extern "C" Q_DECL_EXPORT
float ritual_ZN12QCTextLayout26calculateVerticalAlignmentEN14QCanvasPainter12TextBaselineERK6QRectFRK13QFontMetricsFS4_(
    QCanvasPainter::TextBaseline baseline,
    const QRectF *rect,
    const QFontMetricsF *metrics,
    const QRectF *layoutRect) {
  return QCTextLayout::calculateVerticalAlignment(
      baseline,
      *rect,
      *metrics,
      *layoutRect);
}

//  std::pair<float, float>
//      QCTextLayout::calculateHorizontalAlignment(QCanvasPainter::TextAlign
//      align, const QRectF &rect, float layoutWidth, const QRectF
//      &layoutRect)
extern "C" Q_DECL_EXPORT
std::pair<float, float> *ritual_ZN12QCTextLayout28calculateHorizontalAlignmentEN14QCanvasPainter9TextAlignERK6QRectFfS4_(
    QCanvasPainter::TextAlign align,
    const QRectF *rect,
    float layoutWidth,
    const QRectF *layoutRect) {
  return new std::pair<float, float>(
      QCTextLayout::calculateHorizontalAlignment(
          align,
          *rect,
          layoutWidth,
          *layoutRect));
}

//  Qt::LayoutDirection
//      QCTextLayout::convertToQtDirection(QCanvasPainter::TextDirection
//      direction)
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZN12QCTextLayout20convertToQtDirectionEN14QCanvasPainter13TextDirectionE(
    QCanvasPainter::TextDirection direction) {
  return QCTextLayout::convertToQtDirection(direction);
}

//  QCTextLayout::~QCTextLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCTextLayoutD1Ev(QCTextLayout *self) {
  delete self;
}

//  a std::pair<float, float> a ritual of QCTextLayout gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCTextLayout__std_pair_float_float(
    std::pair<float, float> *self) {
  delete self;
}
