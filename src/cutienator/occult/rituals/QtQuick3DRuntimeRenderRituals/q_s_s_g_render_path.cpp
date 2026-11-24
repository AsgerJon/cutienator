//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererutil_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererutil_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSSGRenderPath::QSSGRenderPath()
extern "C" Q_DECL_EXPORT
QSSGRenderPath *ritual_ZN14QSSGRenderPathC1Ev() {
  return new QSSGRenderPath();
}

//  QSSGRenderPath::QSSGRenderPath(const QString &p, const QString
//      &lightmapKey)
extern "C" Q_DECL_EXPORT
QSSGRenderPath *ritual_ZN14QSSGRenderPathC1ERK7QStringS2_(
    const QString *p,
    const QString *lightmapKey) {
  return new QSSGRenderPath(*p, *lightmapKey);
}

//  bool QSSGRenderPath::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRenderPath6isNullEv(const QSSGRenderPath *self) {
  return self->isNull();
}

//  bool QSSGRenderPath::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRenderPath7isEmptyEv(const QSSGRenderPath *self) {
  return self->isEmpty();
}

//  QString QSSGRenderPath::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSSGRenderPath4pathEv(const QSSGRenderPath *self) {
  return new QString(self->path());
}

//  bool operator==(const QSSGRenderPath &p1, const QSSGRenderPath &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QSSGRenderPathS1_(
    const QSSGRenderPath *p1,
    const QSSGRenderPath *p2) {
  return operator==(*p1, *p2);
}

//  bool operator!=(const QSSGRenderPath &p1, const QSSGRenderPath &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QSSGRenderPathS1_(
    const QSSGRenderPath *p1,
    const QSSGRenderPath *p2) {
  return operator!=(*p1, *p2);
}

//  QSSGRenderPath::~QSSGRenderPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderPathD1Ev(QSSGRenderPath *self) {
  delete self;
}
