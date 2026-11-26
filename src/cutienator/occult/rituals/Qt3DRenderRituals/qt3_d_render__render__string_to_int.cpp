//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/stringtoint_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/stringtoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>

//  int Qt3DRender::Render::StringToInt::lookupId(const QString &str)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render11StringToInt8lookupIdERK7QString(
    const QString *str) {
  return Qt3DRender::Render::StringToInt::lookupId(*str);
}

//  int Qt3DRender::Render::StringToInt::lookupId(QLatin1String str)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render11StringToInt8lookupIdE13QLatin1String(
    const QLatin1String *str) {
  return Qt3DRender::Render::StringToInt::lookupId(*str);
}

//  QString Qt3DRender::Render::StringToInt::lookupString(int idx)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render11StringToInt12lookupStringEi(int idx) {
  return new QString(Qt3DRender::Render::StringToInt::lookupString(idx));
}

//  Qt3DRender::Render::StringToInt::~StringToInt()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11StringToIntD1Ev(
    Qt3DRender::Render::StringToInt *self) {
  delete self;
}
