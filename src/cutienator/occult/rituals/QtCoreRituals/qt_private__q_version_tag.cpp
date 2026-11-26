//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qversiontagging.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(version_tagging)
#if !defined(QVERSIONTAGGING_H)
#include <QtCore/qglobal.h>

//  QtPrivate::QVersionTag::QVersionTag(const void *sym, int currentVersion)
extern "C" Q_DECL_EXPORT
QtPrivate::QVersionTag *ritual_ZN9QtPrivate11QVersionTagC1EPKvi(
    const void *sym,
    int currentVersion) {
  return new QtPrivate::QVersionTag(sym, currentVersion);
}

//  QtPrivate::QVersionTag::~QVersionTag()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate11QVersionTagD1Ev(QtPrivate::QVersionTag *self) {
  delete self;
}

#endif  // !defined(QVERSIONTAGGING_H)
#endif  // QT_CONFIG(version_tagging)
