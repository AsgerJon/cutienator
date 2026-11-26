//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mdiarea)
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qmdiarea_p.h>
#include <QtWidgets/QApplication>
#include <QtWidgets/QStyle>
#include <QtCore/QChildEvent>
#include <QtGui/QResizeEvent>
#include <QtWidgets/QScrollBar>
#include <QtCore/QtAlgorithms>
#include <QtGui/QPainter>
#include <QtGui/QFontMetrics>
#include <QtWidgets/QStyleOption>
#include <QtCore/QDebug>
#include <QtCore/qmath.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtWidgets/private/qlayoutengine_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qmdiarea.cpp, line 503, as _ZNK4QMdi16MinOverlapPlacer5placeERK5QSizeRK5QListI5QRectERKS5_
namespace QMdi {
using namespace Qt::StringLiterals;
inline QPoint MinOverlapPlacer::place(const QSize &size, const QList<QRect> &rects,
                               const QRect &domain) const
{
    if (size.isEmpty() || !domain.isValid())
        return QPoint();
    for (const QRect &rect : rects) {
        if (!rect.isValid())
            return QPoint();
    }

    QList<QRect> candidates = getCandidatePlacements(size, rects, domain);
    return findBestPlacement(domain, rects, candidates);
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdiarea.cpp, line 364, as _ZN4QMdi16MinOverlapPlacer18accumulatedOverlapERK5QRectRK5QListIS1_E
namespace QMdi {
using namespace Qt::StringLiterals;
inline int MinOverlapPlacer::accumulatedOverlap(const QRect &source, const QList<QRect> &rects)
{
    int accOverlap = 0;
    for (const QRect &rect : rects) {
        QRect intersection = source.intersected(rect);
        accOverlap += intersection.width() * intersection.height();
    }
    return accOverlap;
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdiarea.cpp, line 380, as _ZN4QMdi16MinOverlapPlacer18findMinOverlapRectERK5QListI5QRectES5_
namespace QMdi {
using namespace Qt::StringLiterals;
inline QRect MinOverlapPlacer::findMinOverlapRect(const QList<QRect> &source, const QList<QRect> &rects)
{
    int minAccOverlap = -1;
    QRect minAccOverlapRect;
    for (const QRect &srcRect : source) {
        const int accOverlap = accumulatedOverlap(srcRect, rects);
        if (accOverlap < minAccOverlap || minAccOverlap == -1) {
            minAccOverlap = accOverlap;
            minAccOverlapRect = srcRect;
        }
    }
    return minAccOverlapRect;
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdiarea.cpp, line 398, as _ZN4QMdi16MinOverlapPlacer22getCandidatePlacementsERK5QSizeRK5QListI5QRectERKS5_
namespace QMdi {
using namespace Qt::StringLiterals;
inline QList<QRect> MinOverlapPlacer::getCandidatePlacements(const QSize &size, const QList<QRect> &rects,
                                                      const QRect &domain)
{
    QList<QRect> result;

    QList<int> xlist;
    xlist.reserve(2 + rects.size());
    xlist << domain.left() << domain.right() - size.width() + 1;

    QList<int> ylist;
    ylist.reserve(2 + rects.size());
    ylist << domain.top();
    if (domain.bottom() - size.height() + 1 >= 0)
        ylist << domain.bottom() - size.height() + 1;

    for (const QRect &rect : rects) {
        xlist << rect.right() + 1;
        ylist << rect.bottom() + 1;
    }

    std::sort(xlist.begin(), xlist.end());
    xlist.erase(std::unique(xlist.begin(), xlist.end()), xlist.end());

    std::sort(ylist.begin(), ylist.end());
    ylist.erase(std::unique(ylist.begin(), ylist.end()), ylist.end());

    result.reserve(ylist.size() * xlist.size());
    for (int y : std::as_const(ylist))
        for (int x : std::as_const(xlist))
            result << QRect(QPoint(x, y), size);
    return result;
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdiarea.cpp, line 484, as _ZN4QMdi16MinOverlapPlacer17findBestPlacementERK5QRectRK5QListIS1_ERS5_
namespace QMdi {
using namespace Qt::StringLiterals;
inline QPoint MinOverlapPlacer::findBestPlacement(const QRect &domain, const QList<QRect> &rects,
                                           QList<QRect> &source)
{
    const QList<QRect> nonInsiders = findNonInsiders(domain, source);

    if (!source.empty())
        return findMinOverlapRect(source, rects).topLeft();

    QList<QRect> maxOverlappers = findMaxOverlappers(domain, nonInsiders);
    return findMinOverlapRect(maxOverlappers, rects).topLeft();
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdiarea.cpp, line 436, as _ZN4QMdi16MinOverlapPlacer15findNonInsidersERK5QRectR5QListIS1_E
namespace QMdi {
using namespace Qt::StringLiterals;
inline QList<QRect> MinOverlapPlacer::findNonInsiders(const QRect &domain, QList<QRect> &source)
{
    const auto containedInDomain =
            [domain](const QRect &srcRect) { return domain.contains(srcRect); };

    const auto firstOut = std::stable_partition(source.begin(), source.end(), containedInDomain);

    QList<QRect> result;
    result.reserve(source.end() - firstOut);
    std::copy(firstOut, source.end(), std::back_inserter(result));

    source.erase(firstOut, source.end());

    return result;
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdiarea.cpp, line 457, as _ZN4QMdi16MinOverlapPlacer18findMaxOverlappersERK5QRectRK5QListIS1_E
namespace QMdi {
using namespace Qt::StringLiterals;
inline QList<QRect> MinOverlapPlacer::findMaxOverlappers(const QRect &domain, const QList<QRect> &source)
{
    QList<QRect> result;
    result.reserve(source.size());

    int maxOverlap = -1;
    for (const QRect &srcRect : source) {
        QRect intersection = domain.intersected(srcRect);
        const int overlap = intersection.width() * intersection.height();
        if (overlap >= maxOverlap || maxOverlap == -1) {
            if (overlap > maxOverlap) {
                maxOverlap = overlap;
                result.clear();
            }
            result << srcRect;
        }
    }

    return result;
}
}  // namespace QMdi
//  -----------------------------------------------------------------------

//  QPoint QMdi::MinOverlapPlacer::place(const QSize &size, const
//      QList<QRect> &rects, const QRect &domain) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK4QMdi16MinOverlapPlacer5placeERK5QSizeRK5QListI5QRectERKS5_(
    const QMdi::MinOverlapPlacer *self,
    const QSize *size,
    const QList<QRect> *rects,
    const QRect *domain) {
  return new QPoint(self->place(*size, *rects, *domain));
}

//  int QMdi::MinOverlapPlacer::accumulatedOverlap(const QRect &source, const
//      QList<QRect> &rects)
extern "C" Q_DECL_EXPORT
int ritual_ZN4QMdi16MinOverlapPlacer18accumulatedOverlapERK5QRectRK5QListIS1_E(
    const QRect *source,
    const QList<QRect> *rects) {
  return QMdi::MinOverlapPlacer::accumulatedOverlap(*source, *rects);
}

//  QRect QMdi::MinOverlapPlacer::findMinOverlapRect(const QList<QRect>
//      &source, const QList<QRect> &rects)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN4QMdi16MinOverlapPlacer18findMinOverlapRectERK5QListI5QRectES5_(
    const QList<QRect> *source,
    const QList<QRect> *rects) {
  return new QRect(
      QMdi::MinOverlapPlacer::findMinOverlapRect(
          *source,
          *rects));
}

//  QList<QRect> QMdi::MinOverlapPlacer::getCandidatePlacements(const QSize
//      &size, const QList<QRect> &rects, const QRect &domain)
extern "C" Q_DECL_EXPORT
QList<QRect> *ritual_ZN4QMdi16MinOverlapPlacer22getCandidatePlacementsERK5QSizeRK5QListI5QRectERKS5_(
    const QSize *size,
    const QList<QRect> *rects,
    const QRect *domain) {
  return new QList<QRect>(
      QMdi::MinOverlapPlacer::getCandidatePlacements(
          *size,
          *rects,
          *domain));
}

//  QPoint QMdi::MinOverlapPlacer::findBestPlacement(const QRect &domain,
//      const QList<QRect> &rects, QList<QRect> &source)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN4QMdi16MinOverlapPlacer17findBestPlacementERK5QRectRK5QListIS1_ERS5_(
    const QRect *domain,
    const QList<QRect> *rects,
    QList<QRect> *source) {
  return new QPoint(
      QMdi::MinOverlapPlacer::findBestPlacement(
          *domain,
          *rects,
          *source));
}

//  QList<QRect> QMdi::MinOverlapPlacer::findNonInsiders(const QRect &domain,
//      QList<QRect> &source)
extern "C" Q_DECL_EXPORT
QList<QRect> *ritual_ZN4QMdi16MinOverlapPlacer15findNonInsidersERK5QRectR5QListIS1_E(
    const QRect *domain,
    QList<QRect> *source) {
  return new QList<QRect>(
      QMdi::MinOverlapPlacer::findNonInsiders(
          *domain,
          *source));
}

//  QList<QRect> QMdi::MinOverlapPlacer::findMaxOverlappers(const QRect
//      &domain, const QList<QRect> &source)
extern "C" Q_DECL_EXPORT
QList<QRect> *ritual_ZN4QMdi16MinOverlapPlacer18findMaxOverlappersERK5QRectRK5QListIS1_E(
    const QRect *domain,
    const QList<QRect> *source) {
  return new QList<QRect>(
      QMdi::MinOverlapPlacer::findMaxOverlappers(
          *domain,
          *source));
}

//  QMdi::MinOverlapPlacer::~MinOverlapPlacer()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QMdi16MinOverlapPlacerD1Ev(QMdi::MinOverlapPlacer *self) {
  delete self;
}

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
