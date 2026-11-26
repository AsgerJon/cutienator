//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmultimedia_ranges_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 3. Kept as it is when the generator runs again.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if !(defined(__cpp_lib_ranges))
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmultimedia_ranges_p.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtMultimediaPrivate::ranges::impl::min_fn::~min_fn()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate6ranges4impl6min_fnD1Ev(
    QtMultimediaPrivate::ranges::impl::min_fn *self) {
  delete self;
}

//  auto QtMultimediaPrivate::ranges::impl::min_fn::operator()<QList<int>&>(QList<int>&) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QtMultimediaPrivate6ranges4impl6min_fnclIR5QListIiEEEDaOT_(
    const QtMultimediaPrivate::ranges::impl::min_fn *self,
    QList<int> *range) {
  return (*self)(*range);
}

//  auto QtMultimediaPrivate::ranges::impl::min_fn::operator()<QList<double>&>(QList<double>&) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK19QtMultimediaPrivate6ranges4impl6min_fnclIR5QListIdEEEDaOT_(
    const QtMultimediaPrivate::ranges::impl::min_fn *self,
    QList<double> *range) {
  return (*self)(*range);
}

//  auto QtMultimediaPrivate::ranges::impl::min_fn::operator()<QList<QString>&>(QList<QString>&) const
extern "C" Q_DECL_EXPORT
QString * ritual_ZNK19QtMultimediaPrivate6ranges4impl6min_fnclIR5QListI7QStringEEEDaOT_(
    const QtMultimediaPrivate::ranges::impl::min_fn *self,
    QList<QString> *range) {
  return new QString((*self)(*range));
}

#endif  // !(defined(__cpp_lib_ranges))
