//  Written by hand on 2026-11-26 from
//  QtQuick/6.12.0/QtQuick/private/qsgcurveprocessor_p.h, Qt 6.12.0, from Qt's
//  source. Kept as it is when the generator runs again. Qt's library
//  offers the class. A 'QQuadPath &' crosses as its address. Not
//  written: 'processFill' and 'processStroke', whose 'std::function'
//  hands Python 'std::array's and, for 'processFill', a 'std::function'
//  of its own to call back, which no ritual of ours runs yet.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if __has_include(<QtQuick/6.12.0/QtQuick/private/qsgcurveprocessor_p.h>)
#include <QtQuick/6.12.0/QtQuick/private/qsgcurveprocessor_p.h>

//  static bool QSGCurveProcessor::solveOverlaps(QQuadPath &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSGCurveProcessor13solveOverlapsER9QQuadPath(
    QQuadPath *path) {
  return QSGCurveProcessor::solveOverlaps(*path);
}

//  static QList<std::pair<int, int>>
//      QSGCurveProcessor::findOverlappingCandidates(const QQuadPath &path)
extern "C" Q_DECL_EXPORT
QList<std::pair<int, int>> *ritual_ZN17QSGCurveProcessor25findOverlappingCandidatesERK9QQuadPath(
    const QQuadPath *path) {
  return new QList<std::pair<int, int>>(
      QSGCurveProcessor::findOverlappingCandidates(*path));
}

//  static bool QSGCurveProcessor::removeNestedSubpaths(QQuadPath &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSGCurveProcessor20removeNestedSubpathsER9QQuadPath(
    QQuadPath *path) {
  return QSGCurveProcessor::removeNestedSubpaths(*path);
}

//  static bool QSGCurveProcessor::solveIntersections(QQuadPath &path, bool
//      removeNestedPaths)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSGCurveProcessor18solveIntersectionsER9QQuadPathb(
    QQuadPath *path,
    bool removeNestedPaths) {
  return QSGCurveProcessor::solveIntersections(*path, removeNestedPaths);
}

//  a QList<std::pair<int, int>> a ritual of QSGCurveProcessor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSGCurveProcessor__QList_std_pair_int_int(
    QList<std::pair<int, int>> *self) {
  delete self;
}

#endif  // __has_include(<QtQuick/6.12.0/QtQuick/private/qsgcurveprocessor_p.h>)
