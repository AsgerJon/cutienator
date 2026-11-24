//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstring.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>

//  QtPrivate::QLatin1StringArg::QLatin1StringArg()
extern "C" Q_DECL_EXPORT
QtPrivate::QLatin1StringArg *ritual_ZN9QtPrivate16QLatin1StringArgC1Ev() {
  return new QtPrivate::QLatin1StringArg();
}

//  QtPrivate::QLatin1StringArg::QLatin1StringArg(QLatin1StringView v)
extern "C" Q_DECL_EXPORT
QtPrivate::QLatin1StringArg *ritual_ZN9QtPrivate16QLatin1StringArgC1E13QLatin1String(
    const QLatin1String *v) {
  return new QtPrivate::QLatin1StringArg(*v);
}

//  QtPrivate::QLatin1StringArg::~QLatin1StringArg()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate16QLatin1StringArgD1Ev(
    QtPrivate::QLatin1StringArg *self) {
  delete self;
}
