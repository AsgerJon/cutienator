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

//  QtMultimediaPrivate::ranges::impl::sort_fn::~sort_fn()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate6ranges4impl7sort_fnD1Ev(
    QtMultimediaPrivate::ranges::impl::sort_fn *self) {
  delete self;
}

//  void QtMultimediaPrivate::ranges::impl::sort_fn::operator()<QList<int>&>(QList<int>&) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QtMultimediaPrivate6ranges4impl7sort_fnclIR5QListIiEEEvOT_(
    const QtMultimediaPrivate::ranges::impl::sort_fn *self,
    QList<int> *range) {
  (*self)(*range);
}

//  void QtMultimediaPrivate::ranges::impl::sort_fn::operator()<QList<double>&>(QList<double>&) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QtMultimediaPrivate6ranges4impl7sort_fnclIR5QListIdEEEvOT_(
    const QtMultimediaPrivate::ranges::impl::sort_fn *self,
    QList<double> *range) {
  (*self)(*range);
}

//  void QtMultimediaPrivate::ranges::impl::sort_fn::operator()<QList<QString>&>(QList<QString>&) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QtMultimediaPrivate6ranges4impl7sort_fnclIR5QListI7QStringEEEvOT_(
    const QtMultimediaPrivate::ranges::impl::sort_fn *self,
    QList<QString> *range) {
  (*self)(*range);
}

#endif  // !(defined(__cpp_lib_ranges))
