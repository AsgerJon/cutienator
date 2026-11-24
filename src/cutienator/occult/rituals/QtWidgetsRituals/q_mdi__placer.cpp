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

//  QPoint QMdi::Placer::place(const QSize &size, const QList<QRect> &rects,
//      const QRect &domain) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK4QMdi6Placer5placeERK5QSizeRK5QListI5QRectERKS5_(
    const QMdi::Placer *self,
    const QSize *size,
    const QList<QRect> *rects,
    const QRect *domain) {
  return new QPoint(self->place(*size, *rects, *domain));
}

//  QMdi::Placer::~Placer()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QMdi6PlacerD1Ev(QMdi::Placer *self) {
  delete self;
}

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
