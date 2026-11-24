//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstring.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>

//  QtPrivate::QAnyStringArg::QAnyStringArg()
extern "C" Q_DECL_EXPORT
QtPrivate::QAnyStringArg *ritual_ZN9QtPrivate13QAnyStringArgC1Ev() {
  return new QtPrivate::QAnyStringArg();
}

//  QtPrivate::QAnyStringArg::QAnyStringArg(QAnyStringView v)
extern "C" Q_DECL_EXPORT
QtPrivate::QAnyStringArg *ritual_ZN9QtPrivate13QAnyStringArgC1E14QAnyStringView(
    const QString *v) {
  return new QtPrivate::QAnyStringArg(QAnyStringView(*v));
}

//  QtPrivate::QAnyStringArg::~QAnyStringArg()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate13QAnyStringArgD1Ev(QtPrivate::QAnyStringArg *self) {
  delete self;
}
