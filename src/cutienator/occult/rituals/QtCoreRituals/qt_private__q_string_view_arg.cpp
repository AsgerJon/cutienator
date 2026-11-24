//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstring.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QtPrivate::QStringViewArg::QStringViewArg()
extern "C" Q_DECL_EXPORT
QtPrivate::QStringViewArg *ritual_ZN9QtPrivate14QStringViewArgC1Ev() {
  return new QtPrivate::QStringViewArg();
}

//  QtPrivate::QStringViewArg::QStringViewArg(QStringView v)
extern "C" Q_DECL_EXPORT
QtPrivate::QStringViewArg *ritual_ZN9QtPrivate14QStringViewArgC1E11QStringView(
    const QString *v) {
  return new QtPrivate::QStringViewArg(QStringView(*v));
}

//  QtPrivate::QStringViewArg::~QStringViewArg()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate14QStringViewArgD1Ev(
    QtPrivate::QStringViewArg *self) {
  delete self;
}
