//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmultimedia_ranges_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 2. Kept as it is when the generator runs again.
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

//  QtMultimediaPrivate::ranges::impl::upper_bound_fn::~upper_bound_fn()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate6ranges4impl14upper_bound_fnD1Ev(
    QtMultimediaPrivate::ranges::impl::upper_bound_fn *self) {
  delete self;
}

//  auto QtMultimediaPrivate::ranges::impl::upper_bound_fn::operator()<QList<int>&,
//      int, std::less<void> >(QList<int>&, int const&,
//      std::less<void>) const
extern "C" Q_DECL_EXPORT
QList<int>::iterator *ritual_ZNK19QtMultimediaPrivate6ranges4impl14upper_bound_fnclIR5QListIiEEiSt4lessIvEEEDaOT_RKT0_T1_(
    const QtMultimediaPrivate::ranges::impl::upper_bound_fn *self,
    QList<int> *range,
    int value) {
  return new QList<int>::iterator((*self)(*range, value));
}

//  auto QtMultimediaPrivate::ranges::impl::upper_bound_fn::operator()<QList<double>&,
//      double, std::less<void> >(QList<double>&, double const&,
//      std::less<void>) const
extern "C" Q_DECL_EXPORT
QList<double>::iterator *ritual_ZNK19QtMultimediaPrivate6ranges4impl14upper_bound_fnclIR5QListIdEEdSt4lessIvEEEDaOT_RKT0_T1_(
    const QtMultimediaPrivate::ranges::impl::upper_bound_fn *self,
    QList<double> *range,
    double value) {
  return new QList<double>::iterator((*self)(*range, value));
}

#endif  // !(defined(__cpp_lib_ranges))
